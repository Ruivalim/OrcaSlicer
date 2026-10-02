# src/libslic3r/Algorithm/LineSplit.hpp

- SplitLineJunction · class · L9-L36 — struct SplitLineJunction
- SplitLineJunction · function · L22-L25 — SplitLineJunction(const Point& p, bool clipped, int64_t src_idx)
- is_src · function · L27-L27 — bool is_src() const { return src_idx >= 0; }
- get_src_index · function · L28-L35 — size_t get_src_index() const
- do_split_line · function · L40-L40 — SplittedLine do_split_line(const ClipperZUtils::ZPath& path, const ExPolygons& clip, bool closed);
- split_line · function · L43-L65 — template<class PathType>
