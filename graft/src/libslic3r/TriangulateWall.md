# src/libslic3r/TriangulateWall.hpp

- Ring · class · L10-L36 — class Ring
- Ring · function · L14-L14 — explicit Ring(size_t from, size_t to) : begin(from), end(to) { init(begin); }
- size · function · L16-L16 — size_t size() const { return end - begin; }
- pos · function · L17-L17 — std::pair<size_t, size_t> pos() const { return {idx, nextidx}; }
- is_lower · function · L18-L18 — bool is_lower() const { return idx < size(); }
- inc · function · L20-L26 — void inc()
- init · function · L28-L33 — void init(size_t pos)
- is_finished · function · L35-L35 — bool is_finished() const { return nextidx == idx; }
- sq_dst · function · L38-L43 — template<class Sc>
- trscore · function · L45-L53 — template<class Sc>
- Triangulator · class · L55-L112 — template<class Sc>
- calc_score · function · L60-L63 — double calc_score() const
- synchronize_rings · function · L65-L80 — void synchronize_rings()
- emplace_indices · function · L82-L88 — void emplace_indices(std::vector<Vec3i32> &indices)
- run · function · L91-L105 — void run(std::vector<Vec3i32> &indices)
- Triangulator · function · L107-L111 — explicit Triangulator(const std::vector<Vec<3, Sc>> *points,
- triangulate_wall · function · L116-L139 — template<class Sc, class I>
