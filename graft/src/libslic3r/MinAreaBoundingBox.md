# src/libslic3r/MinAreaBoundingBox.hpp

- Polygon · class · L8-L8 — class Polygon;
- ExPolygon · class · L9-L9 — class ExPolygon;
- remove_collinear_points · function · L11-L11 — void remove_collinear_points(Polygon& p);
- remove_collinear_points · function · L12-L12 — void remove_collinear_points(ExPolygon& p);
- MinAreaBoundigBox · class · L18-L51 — class MinAreaBoundigBox
- PolygonLevel · type · L24-L26 — enum PolygonLevel
- MinAreaBoundigBox · function · L31-L31 — explicit MinAreaBoundigBox(const Polygon&, PolygonLevel = pcSimple);
- MinAreaBoundigBox · function · L32-L32 — explicit MinAreaBoundigBox(const ExPolygon&, PolygonLevel = pcSimple);
- MinAreaBoundigBox · function · L33-L33 — explicit MinAreaBoundigBox(const Points&, PolygonLevel = pcSimple);
- angle_to_X · function · L37-L37 — double angle_to_X()  const;
- width · function · L40-L40 — long double width()  const;
- height · function · L43-L43 — long double height() const;
- area · function · L46-L46 — long double area()   const;
- axis · function · L50-L50 — const Point& axis()  const { return m_axis; }
