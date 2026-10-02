# src/libslic3r/GCode/ExtrusionProcessor.hpp

- ExtendedPoint · class · L31-L36 — template<int Dim> struct ExtendedPoint
- estimate_points_properties · function · L38-L391 — template<bool SCALED_INPUT, bool ADD_INTERSECTIONS, bool PREV_LAYER_BOUNDARY_OFFSET, bool SIGNED_DISTANCE, typename POINTS, typename L>
- Subspan · class · L153-L153 — struct Subspan { double t0, t1; int depth; };
- ProcessedPoint · class · L393-L398 — struct ProcessedPoint
- ExtrusionQualityEstimator · class · L400-L567 — class ExtrusionQualityEstimator
- set_current_object · function · L409-L409 — void set_current_object(const PrintObject *object) { current_object = object; }
- prepare_for_new_layer · function · L411-L419 — void prepare_for_new_layer(const PrintObject * obj, const Layer *layer)
- estimate_extrusion_quality · function · L421-L566 — std::vector<ProcessedPoint> estimate_extrusion_quality(const ExtrusionPath                &path,
