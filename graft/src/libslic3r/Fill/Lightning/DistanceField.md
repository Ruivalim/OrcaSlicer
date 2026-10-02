# src/libslic3r/Fill/Lightning/DistanceField.hpp

- DistanceField · class · L24-L205 — class DistanceField
- DistanceField · function · L35-L35 — DistanceField(const coord_t& radius, const Polygons& current_outline, const BoundingBox& current_outlines_bbox, const Polygons& current_overhang);
- tryGetNextPoint · function · L43-L54 — bool tryGetNextPoint(Point *out_unsupported_location, size_t *out_unsupported_cell_idx, const size_t start_idx = 0) const
- update · function · L68-L68 — void update(const Point& to_node, const Point& added_leaf);
- UnsupportedCell · class · L86-L92 — struct UnsupportedCell
- UnsupportedPointsGrid · class · L110-L184 — class UnsupportedPointsGrid
- UnsupportedPointsGrid · function · L113-L113 — UnsupportedPointsGrid() = default;
- initialize · function · L114-L136 — void initialize(const std::vector<UnsupportedCell> &unsupported_points, const std::function<Point(const Point &)> &map_cell_to_grid)
- size · function · L138-L138 — size_t size() const { return m_size; }
- find_cell_idx · function · L140-L151 — size_t find_cell_idx(const Point &grid_addr)
- mark_erased · function · L153-L165 — void mark_erased(const Point &grid_addr)
- map_to_flat_array · function · L176-L183 — inline size_t map_to_flat_array(const Point &loc) const
- to_grid_point · function · L191-L193 — Point to_grid_point(const Point &point) const
- from_grid_point · function · L198-L200 — Point from_grid_point(const Point &point) const
- export_distance_field_to_svg · function · L203-L203 — friend void export_distance_field_to_svg(const std::string &path, const Polygons &outline, const Polygons &overhang, const std::list<DistanceField::UnsupportedCell> &unsupported_points, const Points &points);
