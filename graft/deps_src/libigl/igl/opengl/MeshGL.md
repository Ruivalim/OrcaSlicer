# deps_src/libigl/igl/opengl/MeshGL.h

- GLint · type · L27-L27 — typedef unsigned int GLint;
- DirtyFlags · type · L31-L49 — enum DirtyFlags
- Dynamic · type · L92-L92 — typedef Eigen::Matrix<float,Eigen::Dynamic,Eigen::Dynamic,Eigen::RowMajor> RowMatrixXf;
- TextGL · class · L105-L119 — struct TextGL
- MeshGL · function · L138-L138 — IGL_INLINE MeshGL();
- init · function · L141-L141 — IGL_INLINE void init();
- free · function · L144-L144 — IGL_INLINE void free();
- init_buffers · function · L147-L147 — IGL_INLINE void init_buffers();
- bind_mesh · function · L150-L150 — IGL_INLINE void bind_mesh();
- draw_mesh · function · L155-L155 — IGL_INLINE void draw_mesh(bool solid);
- bind_overlay_lines · function · L158-L158 — IGL_INLINE void bind_overlay_lines();
- draw_overlay_lines · function · L161-L161 — IGL_INLINE void draw_overlay_lines();
- bind_overlay_points · function · L164-L164 — IGL_INLINE void bind_overlay_points();
- draw_overlay_points · function · L167-L167 — IGL_INLINE void draw_overlay_points();
- init_text_rendering · function · L170-L170 — IGL_INLINE void init_text_rendering();
- bind_labels · function · L172-L172 — IGL_INLINE void bind_labels(const TextGL& labels);
- draw_labels · function · L174-L174 — IGL_INLINE void draw_labels(const TextGL& labels);
- free_buffers · function · L177-L177 — IGL_INLINE void free_buffers();
