# src/slic3r/GUI/TextLines.hpp

- ModelVolume · class · L12-L12 — class ModelVolume;
- ModelVolumePtrs · type · L13-L13 — typedef std::vector<ModelVolume *> ModelVolumePtrs;
- TextLinesModel · class · L17-L46 — class TextLinesModel
- init · function · L27-L27 — void init(const Transform3d &text_tr, const ModelVolumePtrs &volumes_to_slice, /*const*/ Emboss::StyleManager &style_manager, unsigned count_lines);
- render · function · L29-L29 — void render(const Transform3d &text_world);
- is_init · function · L31-L31 — bool is_init() const { return m_model.is_initialized(); }
- reset · function · L32-L32 — void reset() { m_model.reset(); m_lines.clear(); }
- get_lines · function · L33-L33 — const Slic3r::Emboss::TextLines &get_lines() const { return m_lines; }
- calc_line_height_in_mm · function · L35-L35 — static double calc_line_height_in_mm(const Slic3r::Emboss::FontFile& ff, const FontProp& fp); // return lineheight in mm
