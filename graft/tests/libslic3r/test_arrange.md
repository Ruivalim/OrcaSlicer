# tests/libslic3r/test_arrange.cpp

- make_square · function · L19-L27 — ArrangePolygon make_square(coord_t side)
- squares · function · L29-L37 — ArrangePolygons squares(int n, double side_mm, double height_mm = 0.)
- bed · function · L40-L43 — BoundingBox bed(double w_mm, double h_mm)
- quiet_params · function · L46-L51 — ArrangeParams quiet_params(coord_t min_dist = 0)
- placed_shapes · function · L53-L60 — ExPolygons placed_shapes(const ArrangePolygons &items)
- overlap_area · function · L64-L73 — double overlap_area(const ExPolygons &shapes)
- disjoint · function · L76-L82 — bool disjoint(const ExPolygons &shapes)
- require_no_overlap · function · L84-L87 — void require_no_overlap(const ArrangePolygons &items)
- seq_print_params · function · L95-L103 — ArrangeParams seq_print_params(coord_t min_dist)
- bed_config · function · L106-L111 — DynamicPrintConfig bed_config()
- squares_of_heights · function · L113-L119 — ArrangePolygons squares_of_heights(const std::vector<double> &heights_mm)
- Case · class · L266-L272 — struct Case
