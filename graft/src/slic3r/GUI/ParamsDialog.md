# src/slic3r/GUI/ParamsDialog.hpp

- Filamentinformation · class · L16-L21 — class Filamentinformation : public wxObject
- ParamsPanel · class · L23-L23 — class ParamsPanel;
- ParamsDialog · class · L25-L43 — class ParamsDialog : public DPIDialog
- ParamsDialog · function · L28-L28 — ParamsDialog(wxWindow * parent);
- panel · function · L30-L30 — ParamsPanel * panel() { return m_panel; }
- Popup · function · L32-L32 — void Popup();
- set_editing_filament_id · function · L34-L34 — void set_editing_filament_id(std::string id) { m_editing_filament_id = id; }
- on_dpi_changed · function · L37-L37 — void on_dpi_changed(const wxRect& suggested_rect) override;
