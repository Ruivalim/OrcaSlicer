# src/slic3r/GUI/PurgeModeDialog.hpp

- wxStaticText · class · L10-L10 — class wxStaticText;
- wxStaticBitmap · class · L11-L11 — class wxStaticBitmap;
- PurgeModeBtnPanel · class · L17-L41 — class PurgeModeBtnPanel : public wxPanel
- PurgeModeBtnPanel · function · L20-L20 — PurgeModeBtnPanel(wxWindow *parent, const wxString &label, const wxString &detail, const std::string &icon_path);
- Select · function · L21-L21 — void Select(bool selected);
- OnPaint · function · L24-L24 — void OnPaint(wxPaintEvent &event);
- OnEnterWindow · function · L27-L27 — void OnEnterWindow(wxMouseEvent &event);
- OnLeaveWindow · function · L28-L28 — void OnLeaveWindow(wxMouseEvent &event);
- UpdateStatus · function · L30-L30 — void UpdateStatus();
- PurgeModeDialogType · type · L43-L46 — enum class PurgeModeDialogType
- PurgeModeDialog · class · L48-L66 — class PurgeModeDialog : public DPIDialog
- PurgeModeDialog · function · L51-L51 — PurgeModeDialog(wxWindow *parent, PurgeModeDialogType dialog_type = PurgeModeDialogType::MultiNozzle);
- get_selected_mode · function · L53-L53 — PrimeVolumeMode get_selected_mode() const { return m_selected_mode; }
- on_dpi_changed · function · L56-L56 — void on_dpi_changed(const wxRect &suggested_rect) override;
- select_option · function · L59-L59 — void select_option(PrimeVolumeMode mode);
- update_panel_selection · function · L60-L60 — void update_panel_selection();
