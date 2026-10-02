"""Tests for orca_filament_automap_plugin_any.py, run against a stand-in `orca` module.

    python3 sandboxes/test_orca_filament_automap.py
"""
import importlib.util
import json
import pathlib
import sys
import types
import unittest


def _install_fake_orca():
    orca = types.ModuleType("orca")

    class _Base:
        def __init__(self):
            self._config = "{}"

        def get_config(self):
            return self._config

        def save_config(self, value):
            self._config = value
            return True

    class _Result:
        @staticmethod
        def success(message=""):
            return ("success", message)

    orca.script = types.SimpleNamespace(ScriptPluginCapabilityBase=_Base)
    orca.base = object
    orca.plugin = lambda cls: cls
    orca.register_capability = lambda cls: None
    orca.ExecutionResult = _Result
    orca.LifecycleEvent = types.SimpleNamespace(FilamentsSynced="FilamentsSynced", PresetSelected="PresetSelected")
    orca.host = types.SimpleNamespace()
    sys.modules["orca"] = orca
    return orca


ORCA = _install_fake_orca()
_SPEC = importlib.util.spec_from_file_location(
    "automap", pathlib.Path(__file__).with_name("orca_filament_automap_plugin_any.py"))
automap = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(automap)


class FakeHost:
    """The slice of orca.host the plugin touches: the bundle, the setter and notifications."""

    def __init__(self, printer, presets, colours_serialized, known=None):
        self.printer = printer
        self.presets = list(presets)
        self.colours_serialized = colours_serialized
        self.known = set(known if known is not None else [])
        self.notifications = []
        host = self

        class Printers:
            def get_selected_preset_name(self):
                return host.printer

        class Bundle:
            printers = Printers()

            def current_filament_preset_names(self):
                return list(host.presets)

            def full_config_value(self, key):
                assert key == "filament_colour"
                return host.colours_serialized

        ORCA.host.preset_bundle = lambda: Bundle()
        ORCA.host.select_filament_preset = self.select
        ORCA.host.ui = types.SimpleNamespace(
            NotificationLevel=types.SimpleNamespace(WarningNotificationLevel="warn", RegularNotificationLevel="info"),
            push_notification=lambda level, text: self.notifications.append((level, text)))

    def select(self, slot, name):
        if name not in self.known or slot >= len(self.presets):
            return False
        self.presets[slot] = name
        return True


def _event(source="full", event="FilamentsSynced"):
    return event, types.SimpleNamespace(source=source)


class ColourParsing(unittest.TestCase):
    def test_normalizes_case_hash_and_alpha(self):
        self.assertEqual(automap.normalize_colour("#ff00aa"), "#FF00AA")
        self.assertEqual(automap.normalize_colour("ff00aa"), "#FF00AA")
        self.assertEqual(automap.normalize_colour("#FF00AA80"), "#FF00AA")

    def test_rejects_what_is_not_a_colour(self):
        for value in ("", None, "#FFF", "#GGGGGG", "red", "#FF00AA0"):
            with self.subTest(value=value):
                self.assertEqual(automap.normalize_colour(value), "")

    def test_an_empty_slot_keeps_its_position(self):
        # A slot with no colour must not shift the colours of the slots after it.
        self.assertEqual(automap.parse_colours('"#FFFFFF";"";"#000000"'), ["#FFFFFF", "", "#000000"])
        self.assertEqual(automap.parse_colours("#ffffff;#000000"), ["#FFFFFF", "#000000"])
        self.assertEqual(automap.parse_colours(None), [])
        self.assertEqual(automap.parse_colours(""), [])


class RuleMatching(unittest.TestCase):
    RULES = [
        {"printer": "", "from": "Generic PETG", "colour": "", "to": "Any PETG"},
        {"printer": "Creality Hi", "from": "Generic PETG", "colour": "#FFFFFF", "to": "Master Print PETG White"},
    ]

    def test_colour_specific_rule_wins_whatever_its_position(self):
        rule = automap.matching_rule(self.RULES, "Creality Hi", "Generic PETG", "#ffffff")
        self.assertEqual(rule["to"], "Master Print PETG White")

    def test_falls_back_to_the_colourless_rule(self):
        rule = automap.matching_rule(self.RULES, "Creality Hi", "Generic PETG", "#000000")
        self.assertEqual(rule["to"], "Any PETG")

    def test_printer_scoped_rule_does_not_leak_to_other_printers(self):
        rule = automap.matching_rule(self.RULES, "Bambu X1C", "Generic PETG", "#FFFFFF")
        self.assertEqual(rule["to"], "Any PETG")
        self.assertIsNone(automap.matching_rule(self.RULES[1:], "Bambu X1C", "Generic PETG", "#FFFFFF"))

    def test_a_colour_rule_does_not_match_a_slot_without_colour(self):
        self.assertIsNone(automap.matching_rule(self.RULES[1:], "Creality Hi", "Generic PETG", ""))

    def test_malformed_rules_are_skipped(self):
        rules = ["junk", None, {"from": "Generic PETG"}, {"from": "Generic PETG", "to": ""}]
        self.assertIsNone(automap.matching_rule(rules, "Creality Hi", "Generic PETG", "#FFFFFF"))

    def test_plan_skips_slots_already_on_the_target(self):
        rules = [{"from": "Generic PLA", "to": "My PLA"}, {"from": "My PLA", "to": "My PLA"}]
        plan = automap.plan_reselections(rules, "P", ["Generic PLA", "My PLA", "Generic ABS"], ["", ""])
        self.assertEqual(plan, [(0, "My PLA")])


class SyncHandling(unittest.TestCase):
    def make(self, config):
        capability = automap.FilamentAutoMap()
        capability.save_config(json.dumps(config))
        return capability

    def test_full_sync_remembers_the_synced_slots_then_reselects(self):
        host = FakeHost("Creality Hi", ["Generic PETG", "Generic PLA"], '"#FFFFFF";"#FF0000"',
                        known={"Master Print PETG White"})
        capability = self.make({"rules": [{"printer": "Creality Hi", "from": "Generic PETG",
                                           "colour": "#FFFFFF", "to": "Master Print PETG White"}]})
        capability.on_lifecycle_event(*_event())

        self.assertEqual(host.presets, ["Master Print PETG White", "Generic PLA"])
        last = json.loads(capability.get_config())["last_sync"]
        # What the printer synced, not what the rules turned it into: that is what new rules match.
        self.assertEqual(last["slots"][0], {"preset": "Generic PETG", "colour": "#FFFFFF"})
        self.assertEqual(host.notifications[-1][0], "info")

    def test_a_refused_preset_is_reported_and_leaves_the_slot(self):
        host = FakeHost("Creality Hi", ["Generic PETG"], '"#FFFFFF"', known=set())
        capability = self.make({"rules": [{"from": "Generic PETG", "to": "Deleted PETG"}]})
        capability.on_lifecycle_event(*_event())

        self.assertEqual(host.presets, ["Generic PETG"])
        level, text = host.notifications[-1]
        self.assertEqual(level, "warn")
        self.assertIn("Deleted PETG", text)

    def test_colour_only_sync_and_other_events_change_nothing(self):
        host = FakeHost("Creality Hi", ["Generic PETG"], '"#FFFFFF"', known={"My PETG"})
        capability = self.make({"rules": [{"from": "Generic PETG", "to": "My PETG"}]})
        capability.on_lifecycle_event(*_event(source="color_only"))
        capability.on_lifecycle_event(*_event(event="PresetSelected"))

        self.assertEqual(host.presets, ["Generic PETG"])
        self.assertIsNone(json.loads(capability.get_config()).get("last_sync"))
        self.assertEqual(host.notifications, [])

    def test_a_corrupt_config_does_not_break_the_sync(self):
        host = FakeHost("Creality Hi", ["Generic PETG"], '"#FFFFFF"', known={"My PETG"})
        capability = automap.FilamentAutoMap()
        capability.save_config("not json")
        capability.on_lifecycle_event(*_event())
        self.assertEqual(host.presets, ["Generic PETG"])

    def test_running_the_capability_applies_rules_to_the_current_slots(self):
        host = FakeHost("Creality Hi", ["Generic PETG"], '"#FFFFFF"', known={"My PETG"})
        capability = self.make({"rules": [{"from": "Generic PETG", "to": "My PETG"}]})
        status, message = capability.execute(None)
        self.assertEqual(status, "success")
        self.assertIn("slot 1 -> My PETG", message)
        self.assertEqual(host.presets, ["My PETG"])


if __name__ == "__main__":
    unittest.main()
