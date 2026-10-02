# src/slic3r/GUI/2DBed.hpp

- Bed_2D · class · L12-L34 — class Bed_2D : public wxPanel
- to_pixels · function · L22-L22 — Point		to_pixels(const Vec2d& point, int height);
- to_pixels · function · L23-L23 — Point       to_pixels(const Point& point, int height);
- set_pos · function · L24-L24 — void		set_pos(const Vec2d& pos);
- Bed_2D · function · L27-L27 — explicit Bed_2D(wxWindow* parent);
- calculate_grid_step · function · L29-L29 — static int calculate_grid_step(const BoundingBox& bb, const double& scale);
- generate_grid · function · L31-L31 — static std::vector<Polylines> generate_grid(const ExPolygon& poly, const BoundingBox& pp_bbox, const Vec2d& origin, const double& step, const double& scale);
- repaint · function · L33-L33 — void repaint(const std::vector<Vec2d>& shape);
