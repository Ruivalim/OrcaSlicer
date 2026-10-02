# tests/libslic3r/test_arachne_walls.cpp

- Segment · class · L41-L68 — struct Segment
- normalized · function · L48-L53 — Segment normalized() const
- points_approx_equal · function · L71-L73 — bool points_approx_equal(const Point& a, const Point& b, coord_t tolerance)
- segments_approx_equal · function · L76-L85 — bool segments_approx_equal(const Segment& a, const Segment& b, coord_t tolerance)
- extract_all_segments · function · L88-L106 — std::vector<Segment> extract_all_segments(const std::vector<VariableWidthLines>& toolpaths)
- find_duplicate_segments · function · L109-L124 — std::vector<std::pair<Segment, Segment>> find_duplicate_segments(
- make_bbl_x1c_028_params · function · L127-L140 — WallToolPathsParams make_bbl_x1c_028_params(int min_bead_width_percent)
- run_arachne_test · function · L144-L203 — size_t run_arachne_test(int min_bead_width_percent)
- wallToolPaths · function · L194-L196 — WallToolPaths wallToolPaths(outline, bead_width_0, bead_width_x,
- InterpolateProbe · class · L274-L276 — struct InterpolateProbe : SkeletalTrapezoidation
- square_loop · function · L318-L322 — Arachne::ExtrusionJunctions square_loop(coord_t width)
- thick_fuzzy_config · function · L324-L338 — FuzzySkinConfig thick_fuzzy_config(FuzzySkinMode mode, NoiseType noise_type, double thickness_mm)
