# src/libslic3r/Clipper2ZUtils.hpp

- zpoint64_lower · function · L16-L18 — inline bool zpoint64_lower(const ZPoint64 &l, const ZPoint64 &r)
- to_zpath64 · function · L22-L32 — template<bool Open = false>
- to_zpath64 · function · L34-L44 — template<bool Open = false>
- to_zpaths64 · function · L47-L54 — template<bool Open = false>
- to_zpaths64 · function · L56-L63 — template<bool Open = false>
- expolygons_to_zpaths64 · function · L67-L80 — template<bool Open = false>
- expolygons_to_zpaths64_with_same_z · function · L83-L95 — template<bool Open = false>
- from_zpath64 · function · L99-L109 — template<bool Open = false>
- from_zpaths64 · function · L112-L117 — template<bool Open = false>
- from_zpaths64 · function · L118-L124 — template<bool Open = false>
- Clipper2ZIntersectionVisitor · class · L127-L164 — class Clipper2ZIntersectionVisitor
- Clipper2ZIntersectionVisitor · function · L133-L133 — Clipper2ZIntersectionVisitor(Intersections &intersections) : m_intersections(intersections) {}
- reset · function · L135-L135 — void reset() { m_intersections.clear(); }
- clipper_callback · function · L153-L158 — auto clipper_callback()
- intersections · function · L160-L160 — const Intersections &intersections() const { return m_intersections; }
