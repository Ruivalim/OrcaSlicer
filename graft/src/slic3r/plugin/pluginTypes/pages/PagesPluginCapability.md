# src/slic3r/plugin/pluginTypes/pages/PagesPluginCapability.hpp

- PagesPluginCapability · class · L12-L30 — class PagesPluginCapability : public PluginCapabilityInterface
- RegisterBindings · function · L15-L15 — static void RegisterBindings(pybind11::module_& module);
- get_type · function · L17-L17 — PluginCapabilityType get_type() const override { return PluginCapabilityType::Pages; }
- get_ui · function · L19-L19 — virtual std::string get_ui() = 0;
- on_message · function · L20-L20 — virtual void on_message(std::string message) { (void) message; }
- get_icon · function · L21-L21 — virtual std::string get_icon() { return {}; }
- post_message · function · L23-L23 — void post_message(std::string message);
- set_message_sender · function · L24-L24 — void set_message_sender(std::function<void(const std::string&)> sender);
- clear_message_sender · function · L25-L25 — void clear_message_sender();
