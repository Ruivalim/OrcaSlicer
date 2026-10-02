# src/libslic3r/Arachne/WallToolPaths.hpp

- meshfix_maximum_resolution · function · L19-L19 — inline coord_t    meshfix_maximum_resolution() { return scaled<coord_t>(0.5); }
- meshfix_maximum_deviation · function · L20-L20 — inline coord_t    meshfix_maximum_deviation() { return scaled<coord_t>(0.025); }
- meshfix_maximum_extrusion_area_deviation · function · L21-L21 — inline coord_t    meshfix_maximum_extrusion_area_deviation() { return scaled<coord_t>(2.); }
- WallToolPathsParams · class · L23-L37 — class WallToolPathsParams
- make_paths_params · function · L39-L39 — WallToolPathsParams make_paths_params(const int layer_id, const PrintObjectConfig &print_object_config, const PrintConfig &print_config);
- WallToolPaths · class · L41-L144 — class WallToolPaths
- WallToolPaths · function · L52-L52 — WallToolPaths(const Polygons& outline, coord_t bead_width_0, coord_t bead_width_x, size_t inset_count, coord_t wall_0_inset, coordf_t layer_height, const WallToolPathsParams &params);
- generate · function · L58-L58 — const std::vector<VariableWidthLines> &generate();
- getToolPaths · function · L64-L64 — const std::vector<VariableWidthLines> &getToolPaths();
- separateOutInnerContour · function · L71-L71 — void separateOutInnerContour();
- getInnerContour · function · L85-L85 — const Polygons& getInnerContour();
- removeEmptyToolPaths · function · L92-L92 — static bool removeEmptyToolPaths(std::vector<VariableWidthLines> &toolpaths);
- getRegionOrder · function · L104-L104 — static ExtrusionLineSet getRegionOrder(const std::vector<ExtrusionLine *> &input, bool outer_to_inner);
- stitchToolPaths · function · L112-L112 — static void stitchToolPaths(std::vector<VariableWidthLines> &toolpaths, coord_t bead_width_x);
- removeSmallLines · function · L117-L117 — void removeSmallLines(std::vector<VariableWidthLines> &toolpaths);
- simplifyToolPaths · function · L126-L126 — static void simplifyToolPaths(std::vector<VariableWidthLines>& toolpaths, const WallToolPathsParams& params);
