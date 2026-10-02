# src/slic3r/GUI/WebPanel.hpp

- WebPanel · class · L16-L46 — class WebPanel : public wxPanel
- WebPanel · function · L19-L19 — WebPanel(wxWindow* parent, const char* bridge_script);
- browser · function · L22-L22 — wxWebView* browser() const { return m_browser; }
- post_to_page · function · L26-L26 — void post_to_page(const std::string& json);
- page_html · function · L30-L30 — virtual std::optional<std::string> page_html() = 0;
- on_page_message · function · L32-L32 — virtual bool on_page_message(const std::string& kind, const nlohmann::json& data) = 0;
- on_load_event · function · L35-L35 — void on_load_event(wxWebViewEvent& event);
- on_navigated · function · L36-L36 — void on_navigated(wxWebViewEvent& event);
- on_script_message · function · L37-L37 — void on_script_message(wxWebViewEvent& event);
- on_webview_recreated · function · L38-L38 — void on_webview_recreated(wxCommandEvent& event);
- apply_theme · function · L39-L39 — void apply_theme();
- load_page_html · function · L40-L40 — void load_page_html();
