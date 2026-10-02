# src/slic3r/GUI/PrivacyUpdateDialog.hpp

- PrivacyUpdateDialog · class · L17-L53 — class PrivacyUpdateDialog : public DPIDialog
- VisibleButtons · type · L20-L24 — enum VisibleButtons { // ORCA VisibleButtons instead ButtonStyle
- PrivacyUpdateDialog · function · L25-L33 — PrivacyUpdateDialog(
- VisibleButtons · type · L29-L29 — enum VisibleButtons btn_style = CONFIRM_AND_CANCEL, // ORCA VisibleButtons instead ButtonStyle
- CreateTipView · function · L34-L34 — wxWebView* CreateTipView(wxWindow* parent);
- OnNavigating · function · L35-L35 — void OnNavigating(wxWebViewEvent& event);
- ShowReleaseNote · function · L36-L36 — bool ShowReleaseNote(std::string content);
- RunScript · function · L37-L37 — void RunScript(std::string script);
- set_text · function · L38-L38 — void set_text(std::string str) { m_mkdown_text = str; };
- on_show · function · L39-L39 — void on_show();
- on_hide · function · L40-L40 — void on_hide();
- update_btn_label · function · L41-L41 — void update_btn_label(wxString ok_btn_text, wxString cancel_btn_text);
- rescale · function · L42-L42 — void rescale();
- on_dpi_changed · function · L44-L44 — void on_dpi_changed(const wxRect& suggested_rect);
