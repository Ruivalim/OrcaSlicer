# src/libslic3r/PolygonTrimmer.hpp

- Grid · class · L15-L15 — class Grid;
- TrimmedLoop · class · L18-L25 — struct TrimmedLoop
- is_trimmed · function · L24-L24 — bool 	is_trimmed() const { return ! segments.empty(); }
- trim_loop · function · L27-L27 — TrimmedLoop trim_loop(const Polygon &loop, const EdgeGrid::Grid &grid);
- trim_loops · function · L28-L28 — std::vector<TrimmedLoop> trim_loops(const Polygons &loops, const EdgeGrid::Grid &grid);
