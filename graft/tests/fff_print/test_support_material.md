# tests/fff_print/test_support_material.cpp

- support_interface_layer_count · function · L22-L25 — static size_t support_interface_layer_count(const std::string &gcode)
- support_base_layer_count · function · L30-L42 — static size_t support_base_layer_count(const std::string &gcode)
- interface_fill_angle_by_layer · function · L47-L69 — static std::map<double, double> interface_fill_angle_by_layer(const std::string &gcode)
- axial_angle_diff_deg · function · L72-L76 — static double axial_angle_diff_deg(double a, double b)
- support_interface_extrusion_length · function · L79-L89 — static double support_interface_extrusion_length(const std::string &gcode)
- support_capital · function · L94-L102 — static TriangleMesh support_capital()
- support_needed_statuses · function · L135-L155 — static std::vector<PrintBase::SlicingStatus> support_needed_statuses(bool no_check)
- lock · function · L150-L150 — std::lock_guard<std::mutex> lock(mutex);
- support_tunnel · function · L263-L268 — static TriangleMesh support_tunnel()
- tunnel_interface_layers · function · L270-L281 — static size_t tunnel_interface_layers(const TriangleMesh &tunnel, int top, int bottom)
