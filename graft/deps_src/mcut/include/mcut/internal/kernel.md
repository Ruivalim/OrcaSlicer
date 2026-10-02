# deps_src/mcut/include/mcut/internal/kernel.h

- class · type · L38-L38 — enum class status_t
- class · type · L78-L78 — enum class cm_patch_location_t : unsigned char
- class · type · L87-L87 — enum class sm_frag_location_t : unsigned char
- class · type · L96-L96 — enum class cm_patch_winding_order_t : unsigned char
- floating_polygon_info_t · class · L101-L107 — struct floating_polygon_info_t
- input_t · class · L112-L156 — struct input_t
- output_mesh_data_maps_t · class · L158-L169 — struct output_mesh_data_maps_t
- output_mesh_info_t · class · L171-L175 — struct output_mesh_info_t
- output_t · class · L180-L210 — struct output_t
- dispatch · function · L213-L213 — void dispatch(output_t& out, const input_t& in);
- point_on_face_plane · function · L223-L223 — bool point_on_face_plane(const hmesh_t& m, const fd_t& f, const vec3& p, int& fv_count);
- to_string · function · L228-L228 — std::string to_string(const sm_frag_location_t&);
- to_string · function · L229-L229 — std::string to_string(const cm_patch_location_t&);
- to_string · function · L230-L230 — std::string to_string(const status_t&);
- to_string · function · L231-L231 — std::string to_string(const cm_patch_winding_order_t&);
