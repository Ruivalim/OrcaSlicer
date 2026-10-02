# src/slic3r/GUI/Widgets/ScrolledWindow.hpp

- MyScrollbar · class · L10-L10 — class MyScrollbar;
- ScrolledWindow · class · L12-L44 — class ScrolledWindow : public wxScrolled<wxWindow>
- ScrolledWindow · function · L15-L15 — ScrolledWindow(wxWindow *parent, wxWindowID id, wxPoint position, wxSize size, long style, int marginWidth = 0, int scrollbarWidth = 4, int tipLength = 0);
- OnMouseWheel · function · L16-L16 — void OnMouseWheel(wxMouseEvent &event);
- SetTipColor · function · L17-L17 — void SetTipColor(wxColour color);
- SetBackgroundColour · function · L18-L18 — bool SetBackgroundColour(const wxColour &color) override;
- SetMarginColor · function · L20-L20 — void         SetMarginColor(wxColour color);
- SetScrollbarColor · function · L21-L21 — void         SetScrollbarColor(wxColour color);
- SetScrollbarTip · function · L22-L22 — void         SetScrollbarTip(int len);
- SetVirtualSize · function · L23-L23 — virtual void SetVirtualSize(int x, int y);
- SetVirtualSize · function · L24-L24 — virtual void SetVirtualSize(wxSize &size);
- GetPanel · function · L25-L25 — wxPanel *    GetPanel() { return m_userPanel; }
- IsBothDirections · function · L28-L28 — bool         IsBothDirections() { return m_bothDirections; }
- SetScrollbars · function · L29-L29 — virtual void SetScrollbars(int pixelsPerUnitX, int pixelsPerUnitY, int noUnitsX, int noUnitsY, int xPos = 0, int yPos = 0, bool noRefresh = false) override;
- OnSize · function · L42-L42 — void OnSize(wxSizeEvent &WXUNUSED(event));
- WXUNUSED · function · L42-L42 — void OnSize(wxSizeEvent &WXUNUSED(event));
- OnScroll · function · L43-L43 — void OnScroll(wxScrollWinEvent &event);
