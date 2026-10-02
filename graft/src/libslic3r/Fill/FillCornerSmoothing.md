# src/libslic3r/Fill/FillCornerSmoothing.hpp

- sanitize_smooth_factor · function · L17-L20 — inline double sanitize_smooth_factor(double smooth_factor)
- CornerSmoother · class · L34-L118 — class CornerSmoother
- CornerSmoother · function · L41-L45 — CornerSmoother(double smooth_factor, double tolerance, double max_corner_distance = 0.,
- enabled · function · L47-L47 — bool enabled() const { return m_corner_distance_ratio > 0.; }
- push · function · L49-L71 — template<typename Emit> void push(const Vec2d &point, Emit &emit)
- flush · function · L74-L81 — template<typename Emit> void flush(Emit &emit)
- emit_corner · function · L84-L89 — template<typename Emit> void emit_corner(const Vec2d &previous, const Vec2d &corner, const Vec2d &next, Emit &emit)
- is_on_straight_run · function · L93-L93 — static bool is_on_straight_run(const Vec2d &previous, const Vec2d &vertex, const Vec2d &next);
- round_corner · function · L95-L95 — void round_corner(const Vec2d &previous, const Vec2d &corner, const Vec2d &next);
- curve_coefficients · function · L98-L98 — const std::vector<Vec2d>& curve_coefficients(double corner_distance, const Vec2d &incoming, const Vec2d &outgoing);
- smooth_polyline_corners · function · L123-L124 — void smooth_polyline_corners(Polyline &polyline, double smooth_factor, double tolerance,
- smooth_polylines_corners · function · L125-L126 — void smooth_polylines_corners(Polylines &polylines, double smooth_factor, double tolerance,
- smooth_polygons_corners · function · L128-L129 — void smooth_polygons_corners(Polygons &polygons, double smooth_factor, double tolerance,
