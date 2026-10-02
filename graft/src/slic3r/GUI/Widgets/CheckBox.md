# src/slic3r/GUI/Widgets/CheckBox.hpp

- CheckBox · class · L8-L56 — class CheckBox : public wxBitmapToggleButton
- CheckBox · function · L11-L11 — CheckBox(wxWindow * parent, int id = wxID_ANY);
- SetValue · function · L14-L14 — void SetValue(bool value) override;
- SetHalfChecked · function · L16-L16 — void SetHalfChecked(bool value = true);
- IsHalfChecked · function · L19-L19 — bool IsHalfChecked() const { return m_half_checked; }
- Rescale · function · L21-L21 — void Rescale();
- Enable · function · L24-L24 — virtual bool Enable(bool enable = true) wxOVERRIDE;
- GetNormalState · function · L29-L29 — virtual State GetNormalState() const wxOVERRIDE;
- DoGetBitmap · function · L33-L33 — virtual wxBitmap DoGetBitmap(State which) const wxOVERRIDE;
- updateBitmap · function · L35-L35 — void updateBitmap(wxEvent & evt);
- update · function · L43-L43 — void update();
