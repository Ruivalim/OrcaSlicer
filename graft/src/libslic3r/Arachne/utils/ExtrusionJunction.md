# src/libslic3r/Arachne/utils/ExtrusionJunction.hpp

- ExtrusionJunction · class · L19-L49 — struct ExtrusionJunction
- ExtrusionJunction · function · L40-L40 — ExtrusionJunction(const Point p, const coord_t w, const coord_t perimeter_index) : p(p), w(w), perimeter_index(perimeter_index) {}
- x · function · L46-L46 — coord_t x() const { return p.x(); }
- y · function · L47-L47 — coord_t y() const { return p.y(); }
- z · function · L48-L48 — coord_t z() const { return w; }
- make_point · function · L57-L57 — inline const Point& make_point(const ExtrusionJunction& ej)
