# src/libslic3r/TexturePainting.hpp

- TriangleMesh · class · L14-L14 — class TriangleMesh;
- ModelVolume · class · L15-L15 — class ModelVolume;
- TextureImage · class · L17-L22 — struct TextureImage
- TexturedMesh · class · L24-L53 — struct TexturedMesh
- has_face_uvs · function · L40-L40 — bool has_face_uvs() const { return !uv_indices.empty() && !uv_coords.empty(); }
- PaintedMesh · class · L55-L60 — struct PaintedMesh
- TexturePaintingSettings · class · L70-L82 — struct TexturePaintingSettings
- MeshRepairDecision · type · L74-L78 — enum class MeshRepairDecision
- FilamentMatch · class · L84-L90 — struct FilamentMatch
- texture_to_painting · function · L92-L97 — bool texture_to_painting(
- face_colors_to_painting · function · L101-L106 — bool face_colors_to_painting(
- match_clusters_to_filaments · function · L109-L112 — std::vector<FilamentMatch> match_clusters_to_filaments(
- compute_delta_e · function · L114-L116 — double compute_delta_e(
- apply_painted_mesh_to_volume · function · L118-L121 — bool apply_painted_mesh_to_volume(
- decode_texture_to_pixels · function · L125-L128 — bool decode_texture_to_pixels(
- sample_original_face_colors · function · L133-L135 — bool sample_original_face_colors(
