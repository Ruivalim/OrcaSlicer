# src/slic3r/GUI/Widgets/LabeledStaticBox.hpp

- LabeledStaticBox · class · L18-L75 — class LabeledStaticBox : public wxStaticBox
- LabeledStaticBox · function · L21-L21 — LabeledStaticBox();
- LabeledStaticBox · function · L23-L29 — LabeledStaticBox(
- Create · function · L31-L37 — bool Create(
- SetCornerRadius · function · L39-L39 — void SetCornerRadius(int radius);
- SetBorderWidth · function · L41-L41 — void SetBorderWidth(int width);
- SetBorderColor · function · L43-L43 — void SetBorderColor(StateColor const &color);
- SetFont · function · L45-L45 — bool SetFont(const wxFont &set_font) override;
- Enable · function · L47-L47 — bool Enable(bool enable) override;
- GetCornerRadius · function · L50-L50 — int        GetCornerRadius() const { return m_radius; }
- GetBorderWidth · function · L51-L51 — int        GetBorderWidth() const  { return m_border_width; }
- GetBorderColor · function · L52-L52 — StateColor GetBorderColor() const  { return border_color; }
- GetScale · function · L53-L53 — float      GetScale() const        { return m_scale; }
- PickDC · function · L56-L56 — void PickDC(wxDC& dc);
- DrawBorderAndLabel · function · L72-L72 — virtual void DrawBorderAndLabel(wxDC& dc);
- GetBordersForSizer · function · L73-L73 — void GetBordersForSizer(int *borderTop, int *borderOther) const override;
