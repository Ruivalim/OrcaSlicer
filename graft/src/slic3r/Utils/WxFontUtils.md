# src/slic3r/Utils/WxFontUtils.hpp

- WxFontUtils · class · L15-L71 — class WxFontUtils
- WxFontUtils · function · L19-L19 — WxFontUtils() = delete;
- can_load · function · L23-L23 — static bool can_load(const wxFont &font);
- create_font_file · function · L26-L26 — static std::unique_ptr<Slic3r::Emboss::FontFile> create_font_file(const wxFont &font);
- get_current_type · function · L28-L28 — static EmbossStyle::Type get_current_type();
- create_emboss_style · function · L29-L29 — static EmbossStyle create_emboss_style(const wxFont &font, const std::string& name = "");
- get_human_readable_name · function · L31-L31 — static std::string get_human_readable_name(const wxFont &font);
- store_wxFont · function · L34-L34 — static std::string store_wxFont(const wxFont &font);
- load_wxFont · function · L35-L35 — static wxFont load_wxFont(const std::string &font_descriptor);
- create_wxFont · function · L38-L38 — static wxFont create_wxFont(const EmbossStyle &style);
- update_property · function · L40-L40 — static void update_property(FontProp &font_prop, const wxFont &font);
- is_italic · function · L42-L42 — static bool is_italic(const wxFont &font);
- is_bold · function · L43-L43 — static bool is_bold(const wxFont &font);
- get_suitable_font_size · function · L45-L45 — static void get_suitable_font_size(int max_height, wxDC &dc);
- set_italic · function · L55-L55 — static std::unique_ptr<Slic3r::Emboss::FontFile> set_italic(wxFont &font, const Slic3r::Emboss::FontFile &prev_font_file);
- set_bold · function · L65-L65 — static std::unique_ptr<Slic3r::Emboss::FontFile> set_bold(wxFont &font, const Slic3r::Emboss::FontFile &font_file);
