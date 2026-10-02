# src/slic3r/GUI/Widgets/StaticLine.hpp

- StaticLine · class · L7-L34 — class StaticLine : public wxWindow
- StaticLine · function · L10-L10 — StaticLine(wxWindow *parent, bool vertical = false, const wxString &label = {}, const wxString &icon = {});
- SetLabel · function · L13-L13 — void SetLabel(const wxString& label) override;
- SetIcon · function · L15-L15 — void SetIcon(const wxString& icon);
- SetLineColour · function · L17-L17 — void SetLineColour(wxColour color);
- Rescale · function · L19-L19 — void Rescale();
- paintEvent · function · L27-L27 — void paintEvent(wxPaintEvent& evt);
- messureSize · function · L29-L29 — void messureSize();
- render · function · L31-L31 — void render(wxDC &dc);
- DECLARE_EVENT_TABLE · function · L33-L33 — DECLARE_EVENT_TABLE()
