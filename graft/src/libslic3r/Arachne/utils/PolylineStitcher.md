# src/libslic3r/Arachne/utils/PolylineStitcher.hpp

- PolylineStitcher · class · L28-L240 — template<typename Paths, typename Path, typename Junction>
- stitch · function · L62-L226 — static void stitch(const Paths& lines, Paths& result_lines, Paths& result_polygons, coord_t max_stitch_distance = scaled<coord_t>(0.1), coord_t snap_distance = scaled<coord_t>(0.01))
- canReverse · function · L231-L231 — static bool canReverse(const PathsPointIndex<Paths> &polyline);
- canConnect · function · L237-L237 — static bool canConnect(const Path &a, const Path &b);
- isOdd · function · L239-L239 — static bool isOdd(const Path &line);
