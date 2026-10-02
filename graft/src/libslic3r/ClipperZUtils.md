# src/libslic3r/ClipperZUtils.hpp

- zpoint_lower · function · L20-L23 — inline bool zpoint_lower(const ZPoint &l, const ZPoint &r)
- to_zpath · function · L27-L39 — template<bool Open = false>
- to_zpaths · function · L43-L51 — template<bool Open = false>
- expolygons_to_zpaths · function · L56-L69 — template<bool Open = false>
- from_zpath · function · L73-L85 — template<bool Open = false>
- from_zpaths · function · L89-L95 — template<bool Open = false>
- from_zpaths · function · L96-L102 — template<bool Open = false>
- ClipperZIntersectionVisitor · class · L104-L139 — class ClipperZIntersectionVisitor
- ClipperZIntersectionVisitor · function · L108-L108 — ClipperZIntersectionVisitor(Intersections &intersections) : m_intersections(intersections) {}
- reset · function · L109-L109 — void reset() { m_intersections.clear(); }
- clipper_callback · function · L129-L133 — ClipperLib_Z::ZFillCallback clipper_callback()
- intersections · function · L135-L135 — const std::vector<std::pair<coord_t, coord_t>>& intersections() const { return m_intersections; }
