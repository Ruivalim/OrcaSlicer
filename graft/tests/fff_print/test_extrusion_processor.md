# tests/fff_print/test_extrusion_processor.cpp

- caged_overhang_mesh · function · L42-L62 — TriangleMesh caged_overhang_mesh()
- outer_wall_feed_rates · function · L91-L107 — template<typename KeepLine> std::vector<double> outer_wall_feed_rates(const std::string& gcode, KeepLine keep_line)
- caged_slope_feed_rates · function · L117-L126 — std::vector<double> caged_slope_feed_rates(const std::string& gcode)
- back_wall_feed_rates · function · L129-L136 — std::vector<double> back_wall_feed_rates(const std::string& gcode)
- cage_shoulder_feed_rates · function · L145-L154 — std::vector<double> cage_shoulder_feed_rates(const std::string& gcode)
- sampled_wall_over_dished_layer · function · L159-L172 — std::vector<ExtendedPoint<2>> sampled_wall_over_dished_layer(const std::function<float(float)>& distance_to_speed)
- sampled_wall_over_narrow_pocket · function · L182-L202 — std::vector<ExtendedPoint<2>> sampled_wall_over_narrow_pocket(
- sampled_wall_between_growing_corners · function · L214-L227 — std::vector<ExtendedPoint<2>> sampled_wall_between_growing_corners(const std::function<float(float)>& distance_to_speed)
- slowed_length · function · L231-L238 — double slowed_length(const std::vector<ExtendedPoint<2>>& points, const std::function<float(float)>& distance_to_speed)
- furthest_reading · function · L240-L245 — float furthest_reading(const std::vector<ExtendedPoint<2>>& points)
- caged_overhang_config · function · L247-L276 — DynamicPrintConfig caged_overhang_config(const char* wall_generator)
- caged_overhang_gcode · function · L278-L285 — std::string caged_overhang_gcode(const char* wall_generator)
- info_feed_rates · function · L289-L296 — void info_feed_rates(const char* span, const std::vector<double>& feed_rates)
- BENCHMARK · function · L437-L440 — BENCHMARK(wall_generator)
