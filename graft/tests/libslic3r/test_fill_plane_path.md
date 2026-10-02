# tests/libslic3r/test_fill_plane_path.cpp

- TestableHilbertCurve · class · L17-L28 — class TestableHilbertCurve : public FillHilbertCurve
- generate_points · function · L20-L27 — Points generate_points(double resolution, double smooth_factor = 0., coord_t max_coordinate = 7)
- output · function · L22-L22 — InfillPolylineOutput output(output_scale);
- TestableOctagramSpiral · class · L30-L41 — class TestableOctagramSpiral : public FillOctagramSpiral
- generate_points · function · L33-L40 — Points generate_points(double resolution, double smooth_factor = 0., coord_t max_coordinate = 7)
- output · function · L35-L35 — InfillPolylineOutput output(output_scale);
- sharpest_turn_cosine · function · L44-L53 — double sharpest_turn_cosine(const Points &points)
- path_length · function · L55-L61 — double path_length(const Points &points)
- discrete_curvature_at · function · L63-L76 — double discrete_curvature_at(const Points &points, const Point &point)
