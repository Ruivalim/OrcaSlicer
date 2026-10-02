# src/libslic3r/JumpPointSearch.hpp

- JPSPathFinder · class · L16-L34 — class JPSPathFinder
- pixelize · function · L25-L25 — Pixel         pixelize(const Point &p) { return p / resolution; }
- unpixelize · function · L26-L26 — Point         unpixelize(const Pixel &p) { return p * resolution; }
- JPSPathFinder · function · L29-L29 — JPSPathFinder() = default;
- init_bed_shape · function · L30-L30 — void     init_bed_shape(const Points &bed_shape) { this->bed_shape = (to_lines(Polygon{bed_shape})); };
- clear · function · L31-L31 — void     clear();
- add_obstacles · function · L32-L32 — void     add_obstacles(const Lines &obstacles);
- find_path · function · L33-L33 — Polyline find_path(const Point &start, const Point &end);
