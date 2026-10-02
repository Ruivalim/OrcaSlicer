# src/libslic3r/MultiMaterialSegmentation.hpp

- ExPolygon · class · L9-L9 — class ExPolygon;
- ModelVolume · class · L10-L10 — class ModelVolume;
- PrintObject · class · L11-L11 — class PrintObject;
- PrintConfig · class · L12-L12 — class PrintConfig;
- PrintObjectConfig · class · L13-L13 — class PrintObjectConfig;
- PrintRegionConfig · class · L14-L14 — class PrintRegionConfig;
- FacetsAnnotation · class · L15-L15 — class FacetsAnnotation;
- ColoredLine · class · L19-L25 — struct ColoredLine
- IncludeTopAndBottomLayers · type · L29-L32 — enum class IncludeTopAndBottomLayers
- ModelVolumeFacetsInfo · class · L34-L40 — struct ModelVolumeFacetsInfo
- segmentation_by_painting · function · L43-L50 — std::vector<std::vector<ExPolygons>> segmentation_by_painting(const PrintObject                                               &print_object,
- multi_material_segmentation_by_painting · function · L53-L53 — std::vector<std::vector<ExPolygons>> multi_material_segmentation_by_painting(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- fuzzy_skin_segmentation_by_painting · function · L56-L56 — std::vector<std::vector<ExPolygons>> fuzzy_skin_segmentation_by_painting(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- resolve_outer_wall_line_width · function · L59-L59 — double resolve_outer_wall_line_width(const PrintRegionConfig &region_config, const PrintObjectConfig &object_config, const PrintConfig &print_config);
- type · type · L66-L66 — typedef segment_concept type;
- coordinate_type · type · L71-L71 — typedef coord_t       coordinate_type;
- point_type · type · L72-L72 — typedef Slic3r::Point point_type;
- get · function · L74-L77 — static inline point_type get(const Slic3r::ColoredLine &line, const direction_1d &dir)
