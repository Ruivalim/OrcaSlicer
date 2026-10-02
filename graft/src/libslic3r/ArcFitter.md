# src/libslic3r/ArcFitter.hpp

- EMovePathType · type · L9-L16 — enum class EMovePathType : unsigned char
- PathFittingData · class · L19-L39 — struct PathFittingData
- is_linear_move · function · L27-L29 — bool is_linear_move()
- is_arc_move · function · L30-L32 — bool is_arc_move()
- reverse_arc_path · function · L33-L38 — bool reverse_arc_path()
- ArcFitter · class · L41-L48 — class ArcFitter
- do_arc_fitting · function · L44-L44 — static void do_arc_fitting(const Points& points, std::vector<PathFittingData> &result, double tolerance);
- do_arc_fitting_and_simplify · function · L47-L47 — static void do_arc_fitting_and_simplify(Points& points, std::vector<PathFittingData>& result, double tolerance);
