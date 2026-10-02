# src/libslic3r/Feature/FuzzySkin/FuzzySkin.hpp

- fuzzy_polyline · function · L10-L10 — void fuzzy_polyline(Points& poly, bool closed, coordf_t slice_z, const FuzzySkinConfig& cfg);
- fuzzy_extrusion_line · function · L12-L12 — void fuzzy_extrusion_line(Arachne::ExtrusionJunctions& ext_lines, coordf_t slice_z, coordf_t layer_height, const FuzzySkinConfig& cfg, bool closed = true);
- group_region_by_fuzzify · function · L14-L14 — void group_region_by_fuzzify(PerimeterGenerator& g);
- should_fuzzify · function · L16-L16 — bool should_fuzzify(const FuzzySkinConfig& config, int layer_id, size_t loop_idx, bool is_contour);
- apply_fuzzy_skin · function · L18-L18 — Polygon apply_fuzzy_skin(const Polygon& polygon, const PerimeterGenerator& perimeter_generator, size_t loop_idx, bool is_contour);
- apply_fuzzy_skin · function · L19-L19 — void    apply_fuzzy_skin(Arachne::ExtrusionLine* extrusion, const PerimeterGenerator& perimeter_generator, bool is_contour, bool closed = true);
