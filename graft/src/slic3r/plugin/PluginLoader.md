# src/slic3r/plugin/PluginLoader.hpp

- load · function · L16-L21 — bool load(const PluginDescriptor&                          descriptor,
- unload · function · L26-L26 — void unload(Plugin& plugin);
- install_packages · function · L30-L30 — bool install_packages(const std::vector<std::string>& pkgs, std::string& error);
- inspect_local_plugin_package · function · L34-L37 — bool inspect_local_plugin_package(const boost::filesystem::path& filepath,
- install_plugin · function · L42-L45 — bool install_plugin(const boost::filesystem::path& filepath,
- install_plugin · function · L46-L46 — bool install_plugin(const boost::filesystem::path& filepath, const std::string& cloud_user_id, std::string& error);
