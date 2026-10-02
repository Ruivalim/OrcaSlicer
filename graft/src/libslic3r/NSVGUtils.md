# src/libslic3r/NSVGUtils.hpp

- NSVGLineParams · class · L18-L44 — struct NSVGLineParams
- NSVGLineParams · function · L40-L43 — explicit NSVGLineParams(double tesselation_tolerance):
- create_shape_with_ids · function · L56-L56 — ExPolygonsWithIds create_shape_with_ids(const NSVGimage &image, const NSVGLineParams &param);
- to_polygons · function · L60-L60 — Polygons to_polygons(const NSVGimage &image, const NSVGLineParams &param);
- bounds · function · L62-L62 — void bounds(const NSVGimage &image, Vec2f &min, Vec2f &max);
- read_from_disk · function · L65-L65 — std::unique_ptr<std::string> read_from_disk(const std::string &path);
- nsvgParseFromFile · function · L68-L68 — NSVGimage_ptr nsvgParseFromFile(const std::string &svg_file_path, const char *units = "mm", float dpi = 96.0f);
- nsvgParse · function · L69-L69 — NSVGimage_ptr nsvgParse(const std::string& file_data, const char *units = "mm", float dpi = 96.0f);
- init_image · function · L70-L70 — NSVGimage *init_image(EmbossShape::SvgFile &svg_file);
- get_shapes_count · function · L77-L77 — size_t get_shapes_count(const NSVGimage &image);
