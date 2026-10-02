# src/libslic3r/Arachne/utils/PolygonsSegmentIndex.hpp

- PolygonsSegmentIndex · class · L17-L26 — class PolygonsSegmentIndex : public PolygonsPointIndex
- PolygonsSegmentIndex · function · L20-L20 — PolygonsSegmentIndex() : PolygonsPointIndex(){};
- PolygonsSegmentIndex · function · L21-L21 — PolygonsSegmentIndex(const Polygons *polygons, unsigned int poly_idx, unsigned int point_idx) : PolygonsPointIndex(polygons, poly_idx, point_idx){};
- from · function · L23-L23 — Point from() const { return PolygonsPointIndex::p(); }
- to · function · L25-L25 — Point to() const { return PolygonsSegmentIndex::next().p(); }
- type · type · L34-L34 — typedef segment_concept type;
- coordinate_type · type · L39-L39 — typedef coord_t       coordinate_type;
- point_type · type · L40-L40 — typedef Slic3r::Point point_type;
- get · function · L42-L45 — static inline point_type get(const Slic3r::Arachne::PolygonsSegmentIndex &CSegment, direction_1d dir)
