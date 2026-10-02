# src/slic3r/GUI/PluginsConfigDialog.hpp

- PluginsConfigDialog · class · L19-L50 — class PluginsConfigDialog : public WebViewHostDialog
- PluginsConfigDialog · function · L22-L22 — PluginsConfigDialog(wxWindow* parent, Preset::Type type, const std::string& overrides_json);
- overrides_json · function · L26-L26 — std::string overrides_json() const { return serialize_plugin_overrides(m_overrides); }
- on_script_message · function · L29-L29 — void on_script_message(const nlohmann::json& payload) override;
- handle_web_command · function · L31-L31 — void handle_web_command(const nlohmann::json& payload);
- current_preset · function · L33-L33 — const Preset* current_preset() const;
- send_capabilities · function · L34-L34 — void          send_capabilities();
- send_capability_config · function · L35-L35 — void          send_capability_config(const PluginCapabilityId& id);
- send_save_error · function · L36-L36 — void          send_save_error(const PluginCapabilityId& id, const std::string& error);
- show_status · function · L37-L37 — void          show_status(const wxString& message, const char* level);
- identifier_from · function · L39-L39 — PluginCapabilityId identifier_from(const nlohmann::json& payload) const;
