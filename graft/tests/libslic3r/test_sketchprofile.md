# tests/libslic3r/test_sketchprofile.cpp

- xy_plane · function · L23-L23 — SketchPlane xy_plane() { return SketchPlane::XY(); }
- line · function · L25-L31 — SketchEntity line(const Vec2d& a, const Vec2d& b)
- rect · function · L34-L38 — std::vector<SketchEntity> rect(double w, double h)
- closed_wires · function · L41-L48 — int closed_wires(const std::vector<SketchEntity>& ents)
- profile_area · function · L52-L60 — double profile_area(const std::vector<SketchEntity>& ents)
- arc · function · L62-L73 — SketchEntity arc(const Vec2d& c, double r, double a0, double a1)
