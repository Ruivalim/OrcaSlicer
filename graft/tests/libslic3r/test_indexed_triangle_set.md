# tests/libslic3r/test_indexed_triangle_set.cpp

- debug_write_obj · function · L35-L44 — void debug_write_obj(const std::vector<indexed_triangle_set> &res, const std::string &name)
- triangle_area · function · L111-L116 — static float triangle_area(const Vec3f &v0, const Vec3f &v1, const Vec3f &v2)
- triangle_area · function · L118-L123 — static float triangle_area(const stl_triangle_vertex_indices &triangle_indices, const std::vector<Vec3f> &vertices)
- create_random_generator · function · L127-L131 — static std::mt19937 create_random_generator()
- gen · function · L129-L129 — std::mt19937 gen(rd());
- its_sample_surface · function · L134-L171 — std::vector<Vec3f> its_sample_surface(const indexed_triangle_set &its,
- CompareConfig · class · L176-L180 — struct CompareConfig
- is_similar · function · L182-L221 — bool is_similar(const indexed_triangle_set &from,
- exist_triangle_with_twice_vertices · function · L289-L296 — bool exist_triangle_with_twice_vertices(const std::vector<stl_triangle_vertex_indices>& indices)
