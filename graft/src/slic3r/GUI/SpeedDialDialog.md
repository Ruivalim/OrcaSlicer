# src/slic3r/GUI/SpeedDialDialog.hpp

- SpeedDialWebDialog · class · L14-L42 — class SpeedDialWebDialog : public WebViewHostDialog
- SpeedDialWebDialog · function · L17-L17 — explicit SpeedDialWebDialog(wxWindow* parent);
- request_show · function · L19-L19 — void request_show();
- add_user_scripts · function · L22-L22 — void add_user_scripts() override;
- on_script_message · function · L23-L23 — void on_script_message(const nlohmann::json& payload) override;
- handle_web_command · function · L24-L24 — void handle_web_command(const nlohmann::json& payload);
- resize_to_content · function · L25-L25 — void resize_to_content(int height);
- run_action · function · L26-L26 — void run_action(const std::string& id, const std::string& title, const std::string& param = "");
- open_wiki · function · L27-L27 — void open_wiki(const std::string& id);
- send_actions · function · L28-L28 — void send_actions();
- search_tabs · function · L29-L29 — void search_tabs();
- apply_rounded_shape · function · L30-L30 — void apply_rounded_shape();
- on_dpi_changed · function · L31-L31 — void on_dpi_changed(const wxRect& suggested_rect) override;
