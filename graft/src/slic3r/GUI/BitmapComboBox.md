# src/slic3r/GUI/BitmapComboBox.hpp

- BitmapComboBox · class · L16-L61 — class BitmapComboBox : public wxBitmapComboBox
- BitmapComboBox · function · L19-L26 — BitmapComboBox(wxWindow* parent,
- Append · function · L30-L30 — int Append(const wxString& item);
- Append · function · L32-L35 — int Append(const wxString& item, const wxBitmap& bitmap)
- OnAddBitmap · function · L50-L50 — bool OnAddBitmap(const wxBitmapBundle& bitmap) override;
- OnDrawItem · function · L51-L51 — void OnDrawItem(wxDC& dc, const wxRect& rect, int item, int flags) const override;
- MSWOnDraw · function · L55-L55 — bool MSWOnDraw(WXDRAWITEMSTRUCT* item) override;
- DrawBackground_ · function · L56-L56 — void DrawBackground_(wxDC& dc, const wxRect& rect, int WXUNUSED(item), int flags) const;
- WXUNUSED · function · L56-L56 — void DrawBackground_(wxDC& dc, const wxRect& rect, int WXUNUSED(item), int flags) const;
- Rescale · function · L58-L58 — void Rescale();
