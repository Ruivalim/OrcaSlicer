# src/slic3r/GUI/ExportPresetBundleDialog.hpp

- ExportCase · type · L29-L38 — enum ExportCase
- ExportPresetBundleDialog · class · L40-L76 — class ExportPresetBundleDialog : public Slic3r::GUI::WebViewHostDialog
- ExportPresetBundleDialog · function · L43-L48 — ExportPresetBundleDialog(wxWindow* parent,
- seq_top_layer_only_changed · function · L53-L53 — bool seq_top_layer_only_changed() const { return m_seq_top_layer_only_changed; }
- recreate_GUI · function · L54-L54 — bool recreate_GUI() const { return m_recreate_GUI; }
- show_export_result · function · L55-L55 — void show_export_result(const ExportCase& e);
- Init · function · L57-L57 — void Init();
- InitExportData · function · L58-L58 — void InitExportData();
- on_script_message · function · L60-L60 — void on_script_message(const nlohmann::json& payload) override;
- OnRequestPresets · function · L61-L61 — void OnRequestPresets();
- OnExportData · function · L62-L62 — void OnExportData(const wxString& path, const wxString& name, json data);
