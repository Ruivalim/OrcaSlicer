# src/slic3r/GUI/DockPanel.hpp

- plugin_pane_name · function · L11-L11 — std::string plugin_pane_name(const std::string& plugin_key, const std::string& title);
- DockPanel · class · L15-L52 — class DockPanel : public WebPanel
- DockPanel · function · L23-L27 — DockPanel(wxWindow*          parent,
- push_message · function · L31-L31 — void push_message(const nlohmann::json& data);
- request_close · function · L33-L33 — void request_close();
- destroy_silently · function · L36-L36 — void destroy_silently();
- fire_close · function · L38-L38 — void fire_close();
- page_html · function · L41-L41 — std::optional<std::string> page_html() override { return m_html; }
- on_page_message · function · L42-L42 — bool on_page_message(const std::string& kind, const nlohmann::json& data) override;
- remove_pane · function · L45-L45 — void remove_pane();
