# src/libslic3r/TextConfiguration.hpp

- FontProp · class · L19-L108 — struct FontProp
- HorizontalAlign · type · L47-L47 — enum class HorizontalAlign { left = 0, center, right };
- VerticalAlign · type · L48-L48 — enum class VerticalAlign { top = 0, center, bottom };
- FontProp · function · L75-L76 — FontProp(float line_height = 10.f) : size_in_mm(line_height), per_glyph(false)
- save · function · L90-L98 — template<class Archive> void save(Archive &ar) const
- load · function · L99-L107 — template<class Archive> void load(Archive &ar)
- EmbossStyle · class · L115-L161 — struct EmbossStyle
- Type · type · L124-L124 — enum class Type;
- Type · type · L135-L147 — enum class Type
- serialize · function · L160-L160 — template<class Archive> void serialize(Archive &ar){ ar(name, path, type, prop); }
- TextConfiguration · class · L173-L183 — struct TextConfiguration
- serialize · function · L182-L182 — template<class Archive> void serialize(Archive &ar) { ar(style, text); }
