# src/slic3r/GUI/OAuthDialog.hpp

- OAuthDialog · class · L11-L29 — class OAuthDialog : public DPIDialog
- on_cancel · function · L19-L19 — void on_cancel(wxEvent& event);
- Show · function · L22-L22 — bool Show(bool show) override;
- on_dpi_changed · function · L23-L23 — void on_dpi_changed(const wxRect& suggested_rect) override;
- OAuthDialog · function · L26-L26 — OAuthDialog(wxWindow* parent, OAuthParams params);
- get_result · function · L28-L28 — OAuthResult get_result() { return *_result; }
