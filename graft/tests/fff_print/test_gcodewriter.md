# tests/fff_print/test_gcodewriter.cpp

- arrange_objects_on_test_bed · function · L26-L30 — static void arrange_objects_on_test_bed(Model &model, const DynamicPrintConfig &config)
- collect_line_args · function · L476-L485 — static std::vector<int> collect_line_args(const std::string &gcode, const std::string &prefix)
- stream · function · L479-L479 — std::istringstream stream(gcode);
- count_lines_with_prefix · function · L487-L490 — static int count_lines_with_prefix(const std::string &gcode, const std::string &prefix)
- ordinals_consecutive · function · L494-L500 — static bool ordinals_consecutive(const std::vector<int> &values)
- dual_extruder_toolchange_config · function · L547-L581 — static DynamicPrintConfig dual_extruder_toolchange_config()
- slice_two_object_bbl · function · L701-L726 — static std::string slice_two_object_bbl(DynamicPrintConfig &config)
- shipped_change_filament_gcode · function · L729-L745 — static std::string shipped_change_filament_gcode(const std::string &printer)
