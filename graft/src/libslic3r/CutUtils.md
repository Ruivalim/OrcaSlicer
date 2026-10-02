# src/libslic3r/CutUtils.hpp

- ModelObjectCutAttribute · type · L14-L14 — enum class ModelObjectCutAttribute : int { KeepUpper, KeepLower, KeepAsParts, FlipUpper, FlipLower, PlaceOnCutUpper, PlaceOnCutLower, CreateDowels, InvalidateCutInfo, KeepPaint };
- Cut · class · L19-L68 — class Cut
- post_process · function · L26-L26 — void post_process(ModelObject* object, ModelObjectPtrs& objects, bool keep, bool place_on_cut, bool flip);
- post_process · function · L27-L27 — void post_process(ModelObject* upper_object, ModelObject* lower_object, ModelObjectPtrs& objects);
- finalize · function · L28-L28 — void finalize(const ModelObjectPtrs& objects, const std::vector<std::optional<TriangleSelector::SavedPainting>>& saved_paintings);
- Cut · function · L32-L35 — Cut(const ModelObject* object, int instance, const Transform3d& cut_matrix,
- Groove · class · L38-L50 — struct Groove
- Part · class · L52-L56 — struct Part
- perform_with_plane · function · L58-L58 — const ModelObjectPtrs& perform_with_plane();
- perform_by_contour · function · L59-L59 — const ModelObjectPtrs& perform_by_contour(const ModelObject* src_object, std::vector<Part> parts, int dowels_count);
- perform_with_groove · function · L60-L65 — const ModelObjectPtrs& perform_with_groove(const Groove&      groove,
- calculate_groove_width · function · L67-L67 — static float calculate_groove_width(const Cut::Groove& groove, const float m_radius);
