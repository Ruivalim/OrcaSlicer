# src/libslic3r/OpenVDBUtils.hpp

- to_vec3f · function · L18-L18 — inline Vec3f to_vec3f(const openvdb::Vec3s &v) { return Vec3f{v.x(), v.y(), v.z()}; }
- to_vec3d · function · L19-L19 — inline Vec3d to_vec3d(const openvdb::Vec3s &v) { return to_vec3f(v).cast<double>(); }
- to_vec3i · function · L20-L20 — inline Vec3i32 to_vec3i(const openvdb::Vec3I &v) { return Vec3i32{int(v[0]), int(v[1]), int(v[2])}; }
- mesh_to_grid · function · L29-L34 — openvdb::FloatGrid::Ptr mesh_to_grid(const indexed_triangle_set &    mesh,
- grid_to_mesh · function · L36-L39 — indexed_triangle_set grid_to_mesh(const openvdb::FloatGrid &grid,
- redistance_grid · function · L41-L44 — openvdb::FloatGrid::Ptr redistance_grid(const openvdb::FloatGrid &grid,
