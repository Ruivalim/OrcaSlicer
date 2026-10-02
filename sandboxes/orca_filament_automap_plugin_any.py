# /// script
# requires-python = ">=3.12"
#
# [tool.orcaslicer.plugin]
# name = "Filament Auto-Map"
# description = "After a printer filament sync, swaps the synced generic presets for your calibrated ones, per printer and colour."
# author = "Rui Valim"
# version = "0.1"
# type = "script"
# ///
"""Filament Auto-Map -- reselect calibrated presets after a printer filament sync.

Syncing filaments from a printer (AMS, CFS, ...) fills each slot with the preset the printer
reports, which for most third-party spools is a "Generic <type>" preset. This plugin keeps a list of
rules -- printer + synced preset + optional colour -> preset to use -- and applies them whenever the
FilamentsSynced lifecycle event fires. The slot keeps the colour the printer reported; only its
preset changes, through orca.host.select_filament_preset().

Rules are edited in the plugin's Config tab. The page lists the slots of the last sync, so a rule is
usually one click away. Running the capability from the Plugins dialog applies the rules to the
current slots without syncing again.

A colour-specific rule wins over one without a colour, whatever their order in the list.
"""
import json

import orca

_DEFAULTS = {
    "rules": [],
    "last_sync": None,
}

_HEX_DIGITS = set("0123456789abcdefABCDEF")


def normalize_colour(value):
    """"#rrggbb" in upper case, or "" for anything that is not a colour. A trailing alpha is dropped."""
    text = str(value or "").strip()
    if text.startswith("#"):
        text = text[1:]
    if len(text) not in (6, 8) or any(ch not in _HEX_DIGITS for ch in text):
        return ""
    return "#" + text[:6].upper()


def parse_colours(serialized):
    """Per-slot colours from full_config_value("filament_colour").

    Vector options come back serialized ('"#FFFFFF";"#000000"'), and a slot without a colour still
    holds its place, so split instead of searching for colours."""
    if not serialized:
        return []
    return [normalize_colour(part.strip().strip('"')) for part in serialized.split(";")]


def matching_rule(rules, printer, preset, colour):
    """The rule that applies to one slot, or None. Colour-specific rules are tried first."""
    candidates = [rule for rule in rules
                  if isinstance(rule, dict)
                  and rule.get("from") == preset
                  and rule.get("to")
                  and (not rule.get("printer") or rule.get("printer") == printer)]
    specific = [rule for rule in candidates if normalize_colour(rule.get("colour"))]
    for rule in specific:
        if normalize_colour(rule.get("colour")) == normalize_colour(colour):
            return rule
    for rule in candidates:
        if not normalize_colour(rule.get("colour")):
            return rule
    return None


def plan_reselections(rules, printer, presets, colours):
    """(slot, preset) for every slot a rule moves to a different preset."""
    plan = []
    for slot, preset in enumerate(presets):
        colour = colours[slot] if slot < len(colours) else ""
        rule = matching_rule(rules, printer, preset, colour)
        if rule is not None and rule["to"] != preset:
            plan.append((slot, rule["to"]))
    return plan


def _load_config(capability):
    try:
        config = json.loads(capability.get_config())
    except (TypeError, ValueError):
        config = {}
    if not isinstance(config, dict):
        config = {}
    merged = dict(_DEFAULTS)
    merged.update(config)
    if not isinstance(merged.get("rules"), list):
        merged["rules"] = []
    return merged


def _current_slots():
    bundle = orca.host.preset_bundle()
    printer = bundle.printers.get_selected_preset_name()
    presets = list(bundle.current_filament_preset_names())
    colours = parse_colours(bundle.full_config_value("filament_colour"))
    return printer, presets, colours


def _notify(text, warning=False):
    level = orca.host.ui.NotificationLevel
    try:
        orca.host.ui.push_notification(level.WarningNotificationLevel if warning else level.RegularNotificationLevel, text)
    except Exception:
        pass  # A notification is a courtesy; the reselection already happened.


def _visible_names(collection, compatible_only):
    user, other = [], []
    for index in range(collection.size()):
        preset = collection.preset(index)
        if not preset.is_visible or preset.is_default or (compatible_only and not preset.is_compatible):
            continue
        (user if preset.is_user() else other).append(preset.name)
    return sorted(user) + sorted(other)


class FilamentAutoMap(orca.script.ScriptPluginCapabilityBase):
    def get_name(self):
        return "Filament Auto-Map"

    def get_default_config(self):
        return _DEFAULTS

    def has_config_ui(self):
        return True

    def get_config_ui(self):
        try:
            bundle = orca.host.preset_bundle()
            printers = _visible_names(bundle.printers, compatible_only=False)
            filaments = _visible_names(bundle.filaments, compatible_only=True)
            current_printer = bundle.printers.get_selected_preset_name()
        except Exception:
            printers, filaments, current_printer = [], [], ""
        data = {"printers": printers, "filaments": filaments, "current_printer": current_printer}
        # The page is inlined into a <script>: escape "<" so a preset name cannot close the tag.
        return _CONFIG_UI.replace("__AUTOMAP_DATA__", json.dumps(data).replace("<", "\\u003c"))

    def execute(self, *args):
        applied, refused = self._apply()
        if not applied and not refused:
            return orca.ExecutionResult.success("Filament Auto-Map: no rule matches the current slots")
        return orca.ExecutionResult.success(self._summary(applied, refused))

    def on_lifecycle_event(self, event, ctx):
        # A colour-only sync keeps the presets on purpose, so leave them alone too.
        if event != orca.LifecycleEvent.FilamentsSynced or ctx.source != "full":
            return
        self._remember_sync()
        applied, refused = self._apply()
        if applied or refused:
            _notify(self._summary(applied, refused), warning=bool(refused))

    def _remember_sync(self):
        printer, presets, colours = _current_slots()
        config = _load_config(self)
        config["last_sync"] = {
            "printer": printer,
            "slots": [{"preset": preset, "colour": colours[slot] if slot < len(colours) else ""}
                      for slot, preset in enumerate(presets)],
        }
        self.save_config(json.dumps(config))

    def _apply(self):
        printer, presets, colours = _current_slots()
        applied, refused = [], []
        for slot, target in plan_reselections(_load_config(self)["rules"], printer, presets, colours):
            if orca.host.select_filament_preset(slot, target):
                applied.append((slot, target))
            else:
                refused.append((slot, target))
        return applied, refused

    @staticmethod
    def _summary(applied, refused):
        parts = []
        if applied:
            parts.append("Filament Auto-Map: " + ", ".join(f"slot {slot + 1} -> {name}" for slot, name in applied))
        if refused:
            parts.append("not applied (missing or incompatible): "
                         + ", ".join(f"slot {slot + 1} -> {name}" for slot, name in refused))
        return "; ".join(parts)


@orca.plugin
class FilamentAutoMapPackage(orca.base):
    def register_capabilities(self):
        orca.register_capability(FilamentAutoMap)


# The Config tab page. It runs in an iframe sandboxed into an opaque origin, so everything it needs
# from the host -- installed printers and filament presets -- is baked in by get_config_ui().
_CONFIG_UI = """
<style>
  :root {
    --ink:   var(--orca-fg, #1f2429);
    --paper: var(--orca-bg, #ffffff);
    --rule:  var(--orca-border, #d9dee3);
    --quiet: var(--orca-muted, #6b7580);
    --live:  var(--orca-accent, #009688);
    --live-ink: var(--orca-accent-fg, #ffffff);
    --ui: var(--orca-font, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  }
  body { margin: 0; padding: 12px; background: var(--paper); color: var(--ink); font: 13px/1.4 var(--ui); }
  h2 { font-size: 13px; margin: 16px 0 6px; }
  h2:first-child { margin-top: 0; }
  p.hint { color: var(--quiet); margin: 0 0 8px; }
  table { width: 100%; border-collapse: collapse; }
  th { text-align: left; font-weight: 600; color: var(--quiet); padding: 4px; border-bottom: 1px solid var(--rule); }
  td { padding: 4px; border-bottom: 1px solid var(--rule); vertical-align: middle; }
  input[type=text] { width: 100%; box-sizing: border-box; padding: 4px; border: 1px solid var(--rule);
                     background: var(--paper); color: var(--ink); font: inherit; }
  .swatch { display: inline-block; width: 14px; height: 14px; border: 1px solid var(--rule); vertical-align: middle; }
  .colour { display: flex; gap: 6px; align-items: center; white-space: nowrap; }
  button { font: inherit; padding: 4px 10px; border: 1px solid var(--rule); background: var(--paper); color: var(--ink); cursor: pointer; }
  button.primary { background: var(--live); color: var(--live-ink); border-color: var(--live); }
  .actions { display: flex; gap: 8px; margin-top: 10px; }
  .empty { color: var(--quiet); padding: 8px 4px; }
</style>

<h2>Last sync</h2>
<p class="hint" id="last-sync-hint">Sync filaments from the printer to list its slots here.</p>
<table id="last-sync" hidden>
  <thead><tr><th>Slot</th><th>Colour</th><th>Synced preset</th><th></th></tr></thead>
  <tbody></tbody>
</table>

<h2>Rules</h2>
<p class="hint">When a synced slot on <em>Printer</em> gets <em>Synced preset</em> (and <em>Colour</em>, if set),
select <em>Use preset</em> instead. Leave Printer empty to match any printer.</p>
<table>
  <thead><tr><th>Printer</th><th>Synced preset</th><th>Colour</th><th>Use preset</th><th></th></tr></thead>
  <tbody id="rules"></tbody>
</table>
<div class="actions">
  <button id="add">Add rule</button>
  <button class="primary" id="save">Save</button>
</div>

<datalist id="printers"></datalist>
<datalist id="filaments"></datalist>

<script>
(function () {
  var data = __AUTOMAP_DATA__;
  var config = { rules: [], last_sync: null };

  function fillList(id, names) {
    var list = document.getElementById(id);
    list.innerHTML = "";
    names.forEach(function (name) {
      var option = document.createElement("option");
      option.value = name;
      list.appendChild(option);
    });
  }
  fillList("printers", data.printers);
  fillList("filaments", data.filaments);

  function textInput(value, listId) {
    var input = document.createElement("input");
    input.type = "text";
    input.value = value || "";
    if (listId) input.setAttribute("list", listId);
    return input;
  }

  function addRuleRow(rule) {
    var row = document.createElement("tr");
    var printer = textInput(rule.printer, "printers");
    var from = textInput(rule.from, "filaments");
    var to = textInput(rule.to, "filaments");

    var colourCell = document.createElement("div");
    colourCell.className = "colour";
    var useColour = document.createElement("input");
    useColour.type = "checkbox";
    useColour.title = "Match this colour only";
    var picker = document.createElement("input");
    picker.type = "color";
    picker.value = rule.colour || "#ffffff";
    useColour.checked = !!rule.colour;
    picker.disabled = !useColour.checked;
    useColour.addEventListener("change", function () { picker.disabled = !useColour.checked; });
    colourCell.appendChild(useColour);
    colourCell.appendChild(picker);

    var remove = document.createElement("button");
    remove.textContent = "Remove";
    remove.addEventListener("click", function () { row.remove(); });

    [printer, from, colourCell, to, remove].forEach(function (element) {
      var cell = document.createElement("td");
      cell.appendChild(element);
      row.appendChild(cell);
    });
    row.readRule = function () {
      return {
        printer: printer.value.trim(),
        from: from.value.trim(),
        colour: useColour.checked ? picker.value.toUpperCase() : "",
        to: to.value.trim()
      };
    };
    document.getElementById("rules").appendChild(row);
  }

  function renderLastSync() {
    var sync = config.last_sync;
    var table = document.getElementById("last-sync");
    var body = table.querySelector("tbody");
    body.innerHTML = "";
    if (!sync || !sync.slots || !sync.slots.length) {
      table.hidden = true;
      document.getElementById("last-sync-hint").hidden = false;
      return;
    }
    table.hidden = false;
    var hint = document.getElementById("last-sync-hint");
    hint.textContent = "Printer: " + sync.printer;
    sync.slots.forEach(function (slot, index) {
      var row = document.createElement("tr");
      var swatch = document.createElement("span");
      swatch.className = "swatch";
      swatch.style.background = slot.colour || "transparent";
      var colour = document.createElement("span");
      colour.className = "colour";
      colour.appendChild(swatch);
      colour.appendChild(document.createTextNode(slot.colour || "-"));
      var make = document.createElement("button");
      make.textContent = "Create rule";
      make.addEventListener("click", function () {
        addRuleRow({ printer: sync.printer, from: slot.preset, colour: slot.colour, to: "" });
      });
      [document.createTextNode(String(index + 1)), colour, document.createTextNode(slot.preset), make]
        .forEach(function (element) {
          var cell = document.createElement("td");
          cell.appendChild(element);
          row.appendChild(cell);
        });
      body.appendChild(row);
    });
  }

  function render(next) {
    config = next || {};
    if (!Array.isArray(config.rules)) config.rules = [];
    document.getElementById("rules").innerHTML = "";
    config.rules.forEach(addRuleRow);
    renderLastSync();
  }

  document.getElementById("add").addEventListener("click", function () {
    addRuleRow({ printer: data.current_printer, from: "", colour: "", to: "" });
  });
  document.getElementById("save").addEventListener("click", function () {
    var rows = Array.prototype.slice.call(document.getElementById("rules").children);
    var rules = rows.map(function (row) { return row.readRule(); })
                    .filter(function (rule) { return rule.from && rule.to; });
    var next = Object.assign({}, config, { rules: rules });
    window.orca.saveConfig(next);
  });

  window.orca.onConfig(render);
})();
</script>
"""
