# src/slic3r/GUI/WebDialog.hpp

- WebDialog · class · L24-L85 — class WebDialog : public Slic3r::GUI::WebViewHostDialog
- WebDialog · function · L35-L43 — WebDialog(wxWindow*          parent,
- post_message · function · L46-L46 — static void post_message(WebDialog* dialog, const nlohmann::json& data);
- request_close · function · L47-L47 — static void request_close(WebDialog* dialog);
- destroy_silently · function · L48-L48 — static void destroy_silently(WebDialog* dialog);
- push_message · function · L52-L52 — void push_message(const nlohmann::json& data);
- is_open · function · L54-L54 — bool is_open() const { return m_open; }
- result · function · L57-L57 — const std::optional<nlohmann::json>& result() const { return m_result; }
- on_script_message · function · L60-L60 — void on_script_message(const nlohmann::json& payload) override;
- append_language_to_url · function · L62-L62 — bool append_language_to_url() const override { return false; }
- add_user_scripts · function · L63-L63 — void add_user_scripts() override;
- on_bootstrap_event · function · L66-L66 — void on_bootstrap_event(wxWebViewEvent& event);
- on_navigated · function · L67-L67 — void on_navigated(wxWebViewEvent& event);
- load_page_html · function · L68-L68 — void load_page_html();
- on_close_window · function · L69-L69 — void on_close_window(wxCloseEvent& event);
- fire_submit · function · L70-L70 — void fire_submit(const nlohmann::json& data);
- fire_close · function · L71-L71 — void fire_close();
- finish · function · L72-L72 — void finish(bool submitted, const nlohmann::json& data);
