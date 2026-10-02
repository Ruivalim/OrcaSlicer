# src/libslic3r/BridgeDetector.hpp

- BridgeDetector · class · L22-L71 — class BridgeDetector
- BridgeDetector · function · L37-L37 — BridgeDetector(ExPolygon _expolygon, const ExPolygons &_lower_slices, coord_t _extrusion_width);
- BridgeDetector · function · L38-L38 — BridgeDetector(const ExPolygons &_expolygons, const ExPolygons &_lower_slices, coord_t _extrusion_width);
- detect_angle · function · L40-L40 — bool detect_angle(double bridge_direction_override = 0.);
- coverage · function · L41-L41 — Polygons coverage(double angle = -1, bool precise = true) const;
- unsupported_edges · function · L42-L42 — void unsupported_edges(double angle, Polylines* unsupported) const;
- unsupported_edges · function · L43-L43 — Polylines unsupported_edges(double angle = -1) const;
- initialize · function · L49-L49 — void initialize();
- BridgeDirection · class · L51-L62 — struct BridgeDirection
- BridgeDirection · function · L52-L52 — BridgeDirection(double a = -1.) : angle(a), coverage(0.), max_length(0.), archored_percent(0.){}
- bridge_direction_candidates · function · L65-L65 — std::vector<double> bridge_direction_candidates() const;
- detect_bridging_direction · function · L75-L119 — inline std::tuple<Vec2d, double> detect_bridging_direction(const Lines &floating_edges, const Polygons &overhang_area)
- detect_bridging_direction · function · L122-L127 — inline std::tuple<Vec2d, double> detect_bridging_direction(const Polygons &to_cover, const Polygons &anchors_area)
