# src/slic3r/GUI/PluginPickerDialog.hpp

- PluginPickerDialog · class · L19-L58 — class PluginPickerDialog : public DPIDialog
- CapabilityEntry · class · L23-L28 — struct CapabilityEntry
- PluginPickerDialog · function · L31-L33 — PluginPickerDialog(wxWindow* parent,
- PluginPickerDialog · function · L36-L38 — PluginPickerDialog(wxWindow* parent,
- selected_plugin_key · function · L41-L41 — std::string selected_plugin_key() const;
- selected_capability · function · L44-L44 — CapabilityEntry selected_capability() const;
- on_dpi_changed · function · L46-L46 — void on_dpi_changed(const wxRect &suggested_rect) override;
- build_ui · function · L49-L49 — void build_ui(const wxString& plugin_type_label);
- build_capability_ui · function · L50-L50 — void build_capability_ui(const wxString& plugin_type_label);
- update_description · function · L51-L51 — void update_description(int selection);
- update_capability_description · function · L52-L52 — void update_capability_description(int selection);
