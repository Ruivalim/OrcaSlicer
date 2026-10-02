# src/slic3r/GUI/Widgets/AxisCtrlButton.hpp

- AxisCtrlButton · class · L11-L78 — class AxisCtrlButton : public wxWindow
- CurrentPos · type · L34-L45 — enum CurrentPos
- AxisCtrlButton · function · L48-L48 — AxisCtrlButton(wxWindow *parent, ScalableBitmap &icon, long style = 0);
- SetMinSize · function · L50-L50 — void SetMinSize(const wxSize& size) override;
- SetTextColor · function · L52-L52 — void SetTextColor(StateColor const& color);
- SetBorderColor · function · L54-L54 — void SetBorderColor(StateColor const& color);
- SetBackgroundColor · function · L56-L56 — void SetBackgroundColor(StateColor const& color);
- SetInnerBackgroundColor · function · L58-L58 — void SetInnerBackgroundColor(StateColor const& color);
- SetBitmap · function · L60-L60 — void SetBitmap(ScalableBitmap &bmp);
- Rescale · function · L62-L62 — void Rescale();
- updateParams · function · L65-L65 — void updateParams();
- paintEvent · function · L67-L67 — void paintEvent(wxPaintEvent& evt);
- render · function · L69-L69 — void render(wxDC& dc);
- mouseDown · function · L71-L71 — void mouseDown(wxMouseEvent& event);
- mouseReleased · function · L72-L72 — void mouseReleased(wxMouseEvent& event);
- mouseMoving · function · L73-L73 — void mouseMoving(wxMouseEvent& event);
- sendButtonEvent · function · L75-L75 — void sendButtonEvent();
- DECLARE_EVENT_TABLE · function · L77-L77 — DECLARE_EVENT_TABLE()
