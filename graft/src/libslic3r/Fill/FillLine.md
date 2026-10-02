# src/libslic3r/Fill/FillLine.hpp

- Surface · class · L10-L10 — class Surface;
- FillLine · class · L12-L46 — class FillLine : public Fill
- clone · function · L15-L15 — Fill* clone() const override { return new FillLine(*this); };
- is_self_crossing · function · L17-L17 — bool is_self_crossing() override { return false; }
- _fill_surface_single · function · L20-L25 — void _fill_surface_single(
- _line · function · L34-L37 — Line _line(int i, coord_t x, coord_t y_min, coord_t y_max) const
- _can_connect · function · L39-L45 — bool _can_connect(coord_t dist_X, coord_t dist_Y)
