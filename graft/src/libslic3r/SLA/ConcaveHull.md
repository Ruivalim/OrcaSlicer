# src/libslic3r/SLA/ConcaveHull.hpp

- get_contours · function · L9-L15 — inline Polygons get_contours(const ExPolygons &poly)
- ConcaveHull · class · L23-L47 — class ConcaveHull
- centroid · function · L26-L26 — static Point centroid(const Points& pp);
- centroid · function · L28-L28 — static inline Point centroid(const Polygon &poly) { return poly.centroid(); }
- calculate_centroids · function · L30-L30 — Points calculate_centroids() const;
- merge_polygons · function · L32-L32 — void merge_polygons();
- add_connector_rectangles · function · L34-L36 — void add_connector_rectangles(const Points &centroids,
- ConcaveHull · function · L39-L40 — ConcaveHull(const ExPolygons& polys, double merge_dist, ThrowOnCancel thr)
- ConcaveHull · function · L42-L42 — ConcaveHull(const Polygons& polys, double mergedist, ThrowOnCancel thr);
- polygons · function · L44-L44 — const Polygons & polygons() const { return m_polys; }
- to_expolygons · function · L46-L46 — ExPolygons to_expolygons() const;
- offset_waffle_style_ex · function · L49-L49 — ExPolygons offset_waffle_style_ex(const ConcaveHull &ccvhull, coord_t delta);
- offset_waffle_style · function · L50-L50 — Polygons   offset_waffle_style(const ConcaveHull &polys, coord_t delta);
