# src/slic3r/GUI/Widgets/Scrollbar.hpp

- ScrolledWindow · class · L14-L14 — class ScrolledWindow;
- MyScrollbar · class · L16-L52 — class MyScrollbar : public wxPanel
- MyScrollbar · function · L19-L19 — MyScrollbar(wxWindow *parent, wxWindowID id, wxPoint position, wxSize size, ScrolledWindow* scrolledWindow, long direction, int scrollbarWidth, int tipLength = 0);
- SetViewStart · function · L20-L20 — void SetViewStart(int start);
- SetTipColor · function · L21-L21 — void SetTipColor(wxColour color);
- SetMarginColor · function · L22-L22 — void SetMarginColor(wxColour color);
- SetScrollbarColor · function · L23-L23 — void SetScrollbarColor(wxColour color);
- SetScrollbarTip · function · L24-L24 — void SetScrollbarTip(int len);
- SetVirtualDim · function · L25-L25 — void SetVirtualDim(int pixelsPerUnit, int noUnits);
- OnPaint · function · L45-L45 — void OnPaint(wxPaintEvent& event);
- OnSize · function · L46-L46 — void OnSize(wxSizeEvent& WXUNUSED(event));
- WXUNUSED · function · L46-L46 — void OnSize(wxSizeEvent& WXUNUSED(event));
- OnEraseBackground · function · L47-L47 — void OnEraseBackground(wxEraseEvent & event);
- OnMouseLeftDown · function · L48-L48 — void OnMouseLeftDown(wxMouseEvent &event);
- OnMouseLeftUp · function · L49-L49 — void OnMouseLeftUp(wxMouseEvent &event);
- OnMouseMove · function · L50-L50 — void OnMouseMove(wxMouseEvent &event);
- OnMouseWheel · function · L51-L51 — void OnMouseWheel(wxMouseEvent &event);
