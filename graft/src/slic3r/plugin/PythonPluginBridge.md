# src/slic3r/plugin/PythonPluginBridge.hpp

- CapturedCapability · class · L14-L18 — struct CapturedCapability
- PythonPluginBridge · class · L20-L46 — class PythonPluginBridge
- instance · function · L23-L23 — static PythonPluginBridge& instance();
- begin_plugin_capture · function · L26-L26 — void begin_plugin_capture(const std::string& plugin_key);
- finalize_plugin_capture · function · L33-L34 — std::vector<CapturedCapability> finalize_plugin_capture(
- cancel_plugin_capture · function · L37-L37 — void cancel_plugin_capture(const std::string& plugin_key);
- clear_pending_captures · function · L40-L40 — void clear_pending_captures();
- PythonPluginBridge · function · L43-L43 — PythonPluginBridge() = default;
- PythonPluginBridge · function · L44-L44 — PythonPluginBridge(const PythonPluginBridge&) = delete;
