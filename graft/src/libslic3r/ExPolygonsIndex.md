# src/libslic3r/ExPolygonsIndex.hpp

- ExPolygonsIndex · class · L11-L27 — struct ExPolygonsIndex
- is_contour · function · L24-L24 — bool is_contour() const { return polygon_index == 0; }
- is_hole · function · L25-L25 — bool is_hole() const { return polygon_index != 0; }
- hole_index · function · L26-L26 — uint32_t hole_index() const { return polygon_index - 1; }
- ExPolygonsIndices · class · L37-L71 — class ExPolygonsIndices
- ExPolygonsIndices · function · L43-L43 — ExPolygonsIndices(const ExPolygons &shapes);
- cvt · function · L50-L50 — uint32_t cvt(const ExPolygonsIndex &id) const;
- cvt · function · L57-L57 — ExPolygonsIndex cvt(uint32_t index) const;
- is_last_point · function · L64-L64 — bool is_last_point(const ExPolygonsIndex &id) const;
- get_count · function · L70-L70 — uint32_t get_count() const;
