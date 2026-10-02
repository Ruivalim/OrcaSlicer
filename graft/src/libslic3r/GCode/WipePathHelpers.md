# src/libslic3r/GCode/WipePathHelpers.hpp

- WipeInwardSupport · class · L13-L17 — struct WipeInwardSupport
- append · function · L16-L16 — void append(const ExtrusionEntity &entity);
- LinesDistancer · class · L20-L20 — template <typename LineType> class LinesDistancer;
- sample_path_at_distance · function · L28-L28 — Point sample_path_at_distance(const ExtrusionPaths &paths, bool forward, double target);
- wipe_offset_direction · function · L32-L32 — int wipe_offset_direction(bool is_ccw, bool is_hole);
- offset_wipe_path · function · L44-L45 — bool offset_wipe_path(Polyline &polyline, Point seam_start, Point seam_end, Point wipe_start,
- wipe_path_support_score · function · L54-L58 — std::optional<double> wipe_path_support_score(
- wipe_path_stays_on_material_side · function · L66-L70 — bool wipe_path_stays_on_material_side(
- offset_wipe_path_toward_support · function · L82-L86 — bool offset_wipe_path_toward_support(Polyline &polyline, Point seam_start, Point seam_end, Point wipe_start,
- wipe_on_loops_destination · function · L93-L94 — std::optional<Point> wipe_on_loops_destination(const ExtrusionPaths &paths, double nozzle_diam_scaled,
