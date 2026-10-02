# tests/slic3rutils/test_plugin_capability_config.cpp

- ScopedPluginManager · class · L39-L48 — struct ScopedPluginManager
- import_orca_module · function · L50-L54 — py::module_ import_orca_module()
- make_capability · function · L58-L80 — py::object make_capability(const std::string& class_name,
- as_interface · function · L82-L85 — std::shared_ptr<PluginCapabilityInterface> as_interface(const py::object& instance)
- host_config · function · L88-L88 — PluginConfig& host_config() { return PluginManager::instance().get_config(); }
- py_get_config · function · L91-L91 — json py_get_config(const py::object& cap) { return json::parse(cap.attr("get_config")().cast<std::string>()); }
- py_save_config · function · L93-L93 — bool py_save_config(const py::object& cap, const json& value) { return cap.attr("save_config")(value.dump()).cast<bool>(); }
- capability_id · function · L95-L98 — PluginCapabilityId capability_id(PluginCapabilityType type, const char* name, const char* plugin_key)
