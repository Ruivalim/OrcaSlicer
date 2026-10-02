# src/slic3r/GUI/Widgets/PopupWindow.hpp

- PopupWindow · class · L7-L41 — class PopupWindow : public wxPopupTransientWindow
- PopupWindow · function · L10-L10 — PopupWindow() {}
- PopupWindow · function · L14-L14 — PopupWindow(wxWindow *parent, int style = wxBORDER_NONE) { Create(parent, style); }
- Create · function · L16-L16 — bool Create(wxWindow *parent, int flags = wxBORDER_NONE);
- BindUnfocusEvent · function · L18-L18 — void BindUnfocusEvent();
- ShouldDismissOnTopWindowDeactivate · function · L25-L25 — virtual bool ShouldDismissOnTopWindowDeactivate() { return true; }
- OnMouseEvent2 · function · L28-L28 — void OnMouseEvent2(wxMouseEvent &evt);
- topWindowActiavate · function · L33-L33 — void topWindowActiavate(wxActivateEvent &event);
- topWindowActivate · function · L37-L37 — void topWindowActivate(wxActivateEvent &event);
- topWindowIconize · function · L38-L38 — void topWindowIconize(wxIconizeEvent &event);
- topWindowShow · function · L39-L39 — void topWindowShow(wxShowEvent &event);
