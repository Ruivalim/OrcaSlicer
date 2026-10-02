# src/libslic3r/Arachne/utils/PolygonsPointIndex.hpp

- make_point · function · L17-L17 — inline const Point &make_point(const Point &p) { return p; }
- PathsPointIndex · class · L22-L128 — template<typename Paths>
- PathsPointIndex · function · L42-L42 — PathsPointIndex() : polygons(nullptr), poly_idx(0), point_idx(0) {}
- PathsPointIndex · function · L50-L50 — PathsPointIndex(const Paths *polygons, unsigned int poly_idx, unsigned int point_idx) : polygons(polygons), poly_idx(poly_idx), point_idx(point_idx) {}
- PathsPointIndex · function · L55-L55 — PathsPointIndex(const PathsPointIndex& original) = default;
- p · function · L57-L63 — Point p() const
- initialized · function · L68-L68 — bool initialized() const { return polygons; }
- getPolygon · function · L73-L73 — const Polygon &getPolygon() const { return (*polygons)[poly_idx]; }
- next · function · L115-L120 — PathsPointIndex next() const
- prev · function · L122-L127 — PathsPointIndex prev() const
- PolygonsPointIndexSegmentLocator · class · L135-L145 — struct PolygonsPointIndexSegmentLocator
- PathsPointIndexLocator · class · L150-L157 — template<typename Paths>
