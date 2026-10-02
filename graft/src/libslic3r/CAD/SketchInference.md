# src/libslic3r/CAD/SketchInference.hpp

- InferenceSnap · class · L17-L25 — struct InferenceSnap
- Kind · type · L18-L18 — enum class Kind { None, Endpoint, Center, Midpoint, OnEdge, Origin };
- snapped · function · L24-L24 — bool snapped() const { return kind != Kind::None; }
- infer_point_snap · function · L31-L33 — InferenceSnap infer_point_snap(const std::vector<SketchEntity>& entities,
- infer_axis_constraint · function · L39-L40 — std::optional<SketchConstraintType>
- infer_relations · function · L48-L51 — std::vector<SketchEntityConstraintDef>
