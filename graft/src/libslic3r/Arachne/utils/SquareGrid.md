# src/libslic3r/Arachne/utils/SquareGrid.hpp

- SquareGrid · class · L28-L109 — class SquareGrid
- SquareGrid · function · L34-L34 — SquareGrid(const coord_t cell_size);
- getCellSize · function · L39-L39 — coord_t getCellSize() const;
- processLineCells · function · L51-L51 — bool processLineCells(const std::pair<Point, Point> line, const std::function<bool (GridPoint)>& process_cell_func);
- processLineCells · function · L60-L60 — bool processLineCells(const std::pair<Point, Point> line, const std::function<bool (GridPoint)>& process_cell_func) const;
- processNearby · function · L74-L74 — bool processNearby(const Point &query_pt, coord_t radius, const std::function<bool(const GridPoint &)> &process_func) const;
- toGridPoint · function · L80-L80 — GridPoint toGridPoint(const Vec2i64 &point) const;
- toGridCoord · function · L86-L86 — grid_coord_t toGridCoord(const int64_t &coord) const;
- toLowerCoord · function · L94-L94 — coord_t toLowerCoord(const grid_coord_t &grid_coord) const;
- nonzeroSign · function · L108-L108 — grid_coord_t nonzeroSign(grid_coord_t z) const;
