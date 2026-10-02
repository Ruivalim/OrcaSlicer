# src/slic3r/Utils/PresetUpdater.hpp

- AppConfig · class · L14-L14 — class AppConfig;
- PresetBundle · class · L15-L15 — class PresetBundle;
- Semver · class · L16-L16 — class Semver;
- PresetUpdater · class · L20-L76 — class PresetUpdater
- PresetUpdater · function · L23-L23 — PresetUpdater();
- PresetUpdater · function · L24-L24 — PresetUpdater(PresetUpdater &&) = delete;
- PresetUpdater · function · L25-L25 — PresetUpdater(const PresetUpdater &) = delete;
- sync · function · L31-L31 — void sync(std::string http_url, std::string language, std::string plugin_version, PresetBundle *preset_bundle);
- slic3r_update_notify · function · L34-L34 — void slic3r_update_notify();
- UpdateResult · type · L36-L44 — enum UpdateResult
- UpdateParams · type · L46-L50 — enum class UpdateParams
- config_update · function · L56-L56 — UpdateResult config_update(const Semver &old_slic3r_version, UpdateParams params) const;
- install_bundles_rsrc · function · L59-L59 — bool install_bundles_rsrc(std::vector<std::string> bundles, bool snapshot = true) const;
- on_update_notification_confirm · function · L61-L61 — void on_update_notification_confirm();
- do_printer_config_update · function · L62-L62 — void do_printer_config_update();
- check_vendor_update · function · L63-L63 — void check_vendor_update(const std::string& vendor_id);
- check_new_vendors · function · L68-L69 — void check_new_vendors(const std::set<std::string>& system_vendors,
- version_check_enabled · function · L71-L71 — bool version_check_enabled() const;
