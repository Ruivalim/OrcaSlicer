# src/slic3r/GUI/SingleChoiceDialog.hpp

- SingleChoiceDialog · class · L10-L23 — class SingleChoiceDialog : public DPIDialog
- SingleChoiceDialog · function · L13-L13 — SingleChoiceDialog(const wxString &message, const wxString &caption, const wxArrayString &choices, int initialSelectionwx, wxWindow *parent = nullptr);
- GetSingleChoiceIndex · function · L16-L16 — int       GetSingleChoiceIndex();
- GetTypeComboBox · function · L17-L17 — ComboBox *GetTypeComboBox() { return type_comboBox; };
- on_dpi_changed · function · L19-L19 — void on_dpi_changed(const wxRect &suggested_rect) override;
