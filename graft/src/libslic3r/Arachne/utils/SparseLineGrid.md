# src/libslic3r/Arachne/utils/SparseLineGrid.hpp

- SparseLineGrid · class · L23-L48 — template<class ElemT, class Locator> class SparseLineGrid : public SparseGrid<ElemT>
- SparseLineGrid · function · L35-L35 — SparseLineGrid(coord_t cell_size, size_t elem_reserve = 0U, float max_load_factor = 1.0f);
- insert · function · L41-L41 — void insert(const Elem &elem);
- process_cell_func · function · L66-L66 — std::function<bool(const GridPoint)> process_cell_func(std::bind(process_cell_func_, m_grid, _1));
