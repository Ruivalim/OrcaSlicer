# src/slic3r/Utils/Obico.hpp

- DynamicPrintConfig · class · L14-L14 — class DynamicPrintConfig;
- Http · class · L15-L15 — class Http;
- Obico · class · L16-L47 — class Obico : public PrintHost
- Obico · function · L19-L19 — Obico(DynamicPrintConfig* config);
- get_name · function · L22-L22 — const char* get_name() const override;
- can_test · function · L23-L23 — virtual bool can_test() const override { return true; };
- has_auto_discovery · function · L24-L24 — bool has_auto_discovery() const override { return false; }
- is_cloud · function · L25-L25 — bool is_cloud() const override { return true; }
- get_login_url · function · L26-L26 — bool get_login_url(wxString& auth_url) const override;
- get_host · function · L27-L27 — std::string  get_host() const override;
- get_test_ok_msg · function · L29-L29 — wxString                           get_test_ok_msg() const override;
- get_test_failed_msg · function · L30-L30 — wxString                           get_test_failed_msg(wxString& msg) const override;
- test · function · L31-L31 — virtual bool                       test(wxString& curl_msg) const override;
- get_printers · function · L32-L32 — bool                               get_printers(wxArrayString& printers) const override;
- get_post_upload_actions · function · L33-L33 — PrintHostPostUploadActions         get_post_upload_actions() const override;
- upload · function · L34-L34 — bool upload(PrintHostUpload upload_data, ProgressFn prorgess_fn, ErrorFn error_fn, InfoFn info_fn) const override;
- set_auth · function · L37-L37 — virtual void set_auth(Http& http) const;
- make_url · function · L46-L46 — std::string make_url(const std::string& path) const;
