# src/slic3r/GUI/Widgets/SideMenuPopup.hpp

- SidePopup · class · L14-L34 — class SidePopup : public PopupWindow
- SidePopup · function · L19-L19 — SidePopup(wxWindow* parent);
- Create · function · L22-L22 — void Create();
- Popup · function · L24-L24 — virtual void Popup(wxWindow *focus = NULL) wxOVERRIDE;
- OnDismiss · function · L25-L25 — virtual void OnDismiss() wxOVERRIDE;
- ProcessLeftDown · function · L26-L26 — virtual bool ProcessLeftDown(wxMouseEvent& event) wxOVERRIDE;
- Show · function · L27-L27 — virtual bool Show(bool show = true) wxOVERRIDE;
- append_button · function · L29-L29 — void append_button(SideButton* btn);
- paintEvent · function · L31-L31 — void paintEvent(wxPaintEvent& evt);
- DECLARE_EVENT_TABLE · function · L33-L33 — DECLARE_EVENT_TABLE()
