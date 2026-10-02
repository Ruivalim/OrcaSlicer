# tests/slic3rutils/test_plugin_lifecycle.cpp

- ScopedPluginManager · class · L42-L52 — struct ScopedPluginManager
- ScopedPluginManager · function · L46-L46 — ScopedPluginManager() { initialized = PluginManager::instance().initialize(); }
- write_plugin · function · L81-L91 — fs::path write_plugin(const ScopedDataDir& data_dir_guard, const std::string& stem, const std::string& source)
- load_and_wait · function · L94-L101 — bool load_and_wait(PluginManager&           manager,
- find_capability · function · L103-L105 — std::shared_ptr<PluginCapabilityInterface> find_capability(PluginManager& manager, const std::string& plugin_key,
- capabilities_of · function · L107-L110 — std::vector<std::shared_ptr<PluginCapabilityInterface>> capabilities_of(PluginManager& manager, const std::string& plugin_key)
- descriptor_of · function · L112-L117 — PluginDescriptor descriptor_of(PluginManager& manager, const std::string& plugin_key)
- lock · function · L131-L131 — std::unique_lock<std::mutex> lock(mutex);
- lock · function · L144-L144 — std::unique_lock<std::mutex> lock(mutex);
- lock · function · L149-L149 — std::lock_guard<std::mutex> lock(mutex);
- lock · function · L160-L160 — std::lock_guard<std::mutex> lock(mutex);
- lock · function · L165-L165 — std::lock_guard<std::mutex> lock(mutex);
- lock · function · L172-L172 — std::unique_lock<std::mutex> lock(mutex);
