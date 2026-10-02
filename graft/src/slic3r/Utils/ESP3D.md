# src/slic3r/Utils/ESP3D.hpp

- DynamicPrintConfig · class · L11-L11 — class DynamicPrintConfig;
- Http · class · L12-L12 — class Http;
- ESP3D · class · L14-L39 — class ESP3D : public PrintHost
- ESP3D · function · L17-L17 — explicit ESP3D(DynamicPrintConfig* config);
- get_name · function · L20-L20 — const char* get_name() const override;
- test · function · L22-L22 — bool                       test(wxString& curl_msg) const override;
- get_test_ok_msg · function · L23-L23 — wxString                   get_test_ok_msg() const override;
- get_test_failed_msg · function · L24-L24 — wxString                   get_test_failed_msg(wxString& msg) const override;
- upload · function · L25-L25 — bool                       upload(PrintHostUpload upload_data, ProgressFn prorgess_fn, ErrorFn error_fn, InfoFn info_fn) const override;
- has_auto_discovery · function · L26-L26 — bool                       has_auto_discovery() const override { return false; }
- can_test · function · L27-L27 — bool                       can_test() const override { return true; }
- get_post_upload_actions · function · L28-L28 — PrintHostPostUploadActions get_post_upload_actions() const override { return PrintHostPostUploadAction::StartPrint; }
- get_host · function · L29-L29 — std::string                get_host() const override { return m_host; }
- start_print · function · L35-L35 — bool        start_print(wxString& msg, const std::string& filename) const;
- get_err_code_from_body · function · L36-L36 — int         get_err_code_from_body(const std::string& body) const;
- get_short_name · function · L37-L37 — std::string get_short_name(const std::string& filename) const;
- format_command · function · L38-L38 — std::string format_command(const std::string& path, const std::string& arg, const std::string& val) const;
