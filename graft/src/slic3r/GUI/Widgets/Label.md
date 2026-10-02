# src/slic3r/GUI/Widgets/Label.hpp

- Label · class · L11-L62 — class Label : public wxStaticText
- Label · function · L14-L14 — Label(wxWindow *parent, wxString const &text = {}, long style = 0, wxSize size = wxDefaultSize);
- Label · function · L16-L16 — Label(wxWindow *parent, wxFont const &font, wxString const &text = {}, long style = 0, wxSize size = wxDefaultSize);
- SetLabel · function · L18-L18 — void SetLabel(const wxString& label) override;
- SetWindowStyleFlag · function · L20-L20 — void SetWindowStyleFlag(long style) override;
- Wrap · function · L22-L22 — void Wrap(int width);
- OnSize · function · L25-L25 — void OnSize(wxSizeEvent & evt);
- initSysFont · function · L57-L57 — static void initSysFont();
- sysFont · function · L59-L59 — static wxFont sysFont(int size, bool bold = false);
- split_lines · function · L61-L61 — static wxSize split_lines(wxDC &dc, int width, const wxString &text, wxString &multiline_text, int max_count = 0);
