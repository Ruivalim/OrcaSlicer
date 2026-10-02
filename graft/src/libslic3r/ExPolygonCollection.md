# src/libslic3r/ExPolygonCollection.hpp

- ExPolygonCollection · class · L11-L11 — class ExPolygonCollection;
- ExPolygonCollections · type · L12-L12 — typedef std::vector<ExPolygonCollection> ExPolygonCollections;
- ExPolygonCollection · class · L14-L35 — class ExPolygonCollection
- ExPolygonCollection · function · L19-L19 — ExPolygonCollection() {}
- ExPolygonCollection · function · L20-L20 — explicit ExPolygonCollection(const ExPolygon &expolygon);
- ExPolygonCollection · function · L21-L21 — explicit ExPolygonCollection(const ExPolygons &expolygons) : expolygons(expolygons) {}
- scale · function · L25-L25 — void scale(double factor);
- translate · function · L26-L26 — void translate(double x, double y);
- rotate · function · L27-L27 — void rotate(double angle, const Point &center);
- contains · function · L28-L28 — template <class T> bool contains(const T &item) const;
- contains_b · function · L29-L29 — bool contains_b(const Point &point) const;
- simplify · function · L30-L30 — void simplify(double tolerance);
- convex_hull · function · L31-L31 — Polygon convex_hull() const;
- lines · function · L32-L32 — Lines lines() const;
- contours · function · L33-L33 — Polygons contours() const;
- append · function · L34-L34 — void append(const ExPolygons &expolygons);
- get_extents · function · L37-L37 — extern BoundingBox get_extents(const ExPolygonCollection &expolygon);
