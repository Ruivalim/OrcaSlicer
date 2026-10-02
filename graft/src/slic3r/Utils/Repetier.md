# src/slic3r/Utils/Repetier.hpp

- DynamicPrintConfig · class · L12-L12 — class DynamicPrintConfig;
- Http · class · L13-L13 — class Http;
- Repetier · class · L15-L44 — class Repetier : public PrintHost
- Repetier · function · L18-L18 — Repetier(DynamicPrintConfig *config);
- get_name · function · L21-L21 — const char* get_name() const override;
- test · function · L23-L23 — bool test(wxString &curl_msg) const override;
- get_test_ok_msg · function · L24-L24 — wxString get_test_ok_msg () const override;
- get_test_failed_msg · function · L25-L25 — wxString get_test_failed_msg (wxString &msg) const override;
- upload · function · L26-L26 — bool upload(PrintHostUpload upload_data, ProgressFn prorgess_fn, ErrorFn error_fn, InfoFn info_fn) const override;
- has_auto_discovery · function · L27-L27 — bool has_auto_discovery() const override { return false; }
- can_test · function · L28-L28 — bool can_test() const override { return true; }
- get_post_upload_actions · function · L29-L29 — PrintHostPostUploadActions get_post_upload_actions() const override { return PrintHostPostUploadAction::StartPrint; }
- supports_multiple_printers · function · L30-L30 — bool supports_multiple_printers() const override { return true; }
- get_host · function · L31-L31 — std::string get_host() const override { return host; }
- get_groups · function · L33-L33 — bool get_groups(wxArrayString &groups) const override;
- get_printers · function · L34-L34 — bool get_printers(wxArrayString &printers) const override;
- set_auth · function · L42-L42 — void set_auth(Http &http) const;
- make_url · function · L43-L43 — std::string make_url(const std::string &path) const;
