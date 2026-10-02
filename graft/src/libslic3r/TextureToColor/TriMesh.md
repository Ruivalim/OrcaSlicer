# src/libslic3r/TextureToColor/TriMesh.hpp

- TriMesh · class · L12-L25 — struct TriMesh : ::indexed_triangle_set
- TriMesh · function · L13-L13 — TriMesh() = default;
- TriMesh · function · L14-L14 — TriMesh(const TriMesh&) = default;
- TriMesh · function · L16-L16 — TriMesh(TriMesh&&) = default;
- TriMesh · function · L18-L18 — TriMesh(const ::indexed_triangle_set& d) : ::indexed_triangle_set(d) {}
- TriMesh · function · L19-L19 — TriMesh(::indexed_triangle_set&& d) : ::indexed_triangle_set(std::move(d)) {}
- TriMesh · function · L20-L22 — TriMesh(std::vector<stl_triangle_vertex_indices> indices_,
- facets_count · function · L24-L24 — std::size_t facets_count() const { return indices.size(); }
