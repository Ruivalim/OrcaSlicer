# src/slic3r/Utils/AstroBox.hpp

- DynamicPrintConfig · class · L12-L12 — class DynamicPrintConfig;
- Http · class · L13-L13 — class Http;
- AstroBox · class · L15-L42 — class AstroBox : public PrintHost
- AstroBox · function · L18-L18 — AstroBox(DynamicPrintConfig *config);
- get_name · function · L21-L21 — const char* get_name() const override;
- test · function · L23-L23 — bool test(wxString &curl_msg) const override;
- get_test_ok_msg · function · L24-L24 — wxString get_test_ok_msg () const override;
- get_test_failed_msg · function · L25-L25 — wxString get_test_failed_msg (wxString &msg) const override;
- upload · function · L26-L26 — bool upload(PrintHostUpload upload_data, ProgressFn prorgess_fn, ErrorFn error_fn, InfoFn info_fn) const override;
- has_auto_discovery · function · L27-L27 — bool has_auto_discovery() const override { return true; }
- can_test · function · L28-L28 — bool can_test() const override { return true; }
- get_post_upload_actions · function · L29-L29 — PrintHostPostUploadActions get_post_upload_actions() const override { return PrintHostPostUploadAction::StartPrint; }
- get_host · function · L30-L30 — std::string get_host() const override { return host; }
- validate_version_text · function · L33-L33 — bool validate_version_text(const boost::optional<std::string> &version_text) const;
- set_auth · function · L40-L40 — void set_auth(Http &http) const;
- make_url · function · L41-L41 — std::string make_url(const std::string &path) const;
