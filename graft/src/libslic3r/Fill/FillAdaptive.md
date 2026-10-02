# src/libslic3r/Fill/FillAdaptive.hpp

- PrintObject · class · L20-L20 — class PrintObject;
- OctreeDeleter · class · L27-L27 — struct OctreeDeleter { void operator()(Octree *p); };
- adaptive_fill_line_spacing · function · L34-L34 — std::pair<double, double>       adaptive_fill_line_spacing(const PrintObject &print_object);
- transform_to_world · function · L37-L37 — Eigen::Quaterniond              transform_to_world();
- transform_to_octree · function · L39-L39 — Eigen::Quaterniond              transform_to_octree();
- build_octree · function · L41-L49 — FillAdaptive::OctreePtr         build_octree(
- Filler · class · L56-L75 — class Filler : public Slic3r::Fill
- clone · function · L62-L62 — Fill* clone() const override { return new Filler(*this); }
- _fill_surface_single · function · L63-L68 — void _fill_surface_single(
- no_sort · function · L73-L73 — bool no_sort() const override { return false; }
- is_self_crossing · function · L74-L74 — bool is_self_crossing() override { return true; }
