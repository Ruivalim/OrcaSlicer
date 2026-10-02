# src/libslic3r/LayOnFace.hpp

- ModelObject · class · L9-L9 — class ModelObject;
- LayOnFacePlane · class · L17-L24 — struct LayOnFacePlane
- lay_on_face_planes · function · L29-L29 — std::vector<LayOnFacePlane> lay_on_face_planes(const ModelObject &object, const Transform3d &instance_matrix_no_offset);
- find_largest_plane · function · L33-L33 — int find_largest_plane(const std::vector<LayOnFacePlane> &planes);
- find_plane_by_normal · function · L37-L37 — int find_plane_by_normal(const std::vector<LayOnFacePlane> &planes, const Vec3d &direction);
- find_plane_at_point · function · L41-L42 — int find_plane_at_point(const std::vector<LayOnFacePlane> &planes, const Transform3d &instance_matrix_no_offset,
- lay_on_face · function · L46-L46 — void lay_on_face(ModelObject &object, size_t instance_idx, const Vec3d &normal);
