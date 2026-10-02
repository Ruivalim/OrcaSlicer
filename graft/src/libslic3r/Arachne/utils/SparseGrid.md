# src/libslic3r/Arachne/utils/SparseGrid.hpp

- SparseGrid · class · L24-L94 — template<class ElemT> class SparseGrid : public SquareGrid
- SparseGrid · function · L43-L43 — SparseGrid(coord_t cell_size, size_t elem_reserve=0U, float max_load_factor=1.0f);
- begin · function · L45-L45 — iterator begin() { return m_grid.begin(); }
- end · function · L46-L46 — iterator end() { return m_grid.end(); }
- begin · function · L47-L47 — const_iterator begin() const { return m_grid.begin(); }
- end · function · L48-L48 — const_iterator end() const { return m_grid.end(); }
- getNearby · function · L65-L65 — std::vector<Elem> getNearby(const Point &query_pt, coord_t radius) const;
- processNearby · function · L80-L80 — bool processNearby(const Point &query_pt, coord_t radius, const std::function<bool(const ElemT &)> &process_func) const;
- processFromCell · function · L90-L90 — bool processFromCell(const GridPoint &grid_pt, const std::function<bool(const Elem &)> &process_func) const;
