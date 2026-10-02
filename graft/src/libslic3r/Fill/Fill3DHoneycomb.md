# src/libslic3r/Fill/Fill3DHoneycomb.hpp

- Fill3DHoneycomb · class · L12-L30 — class Fill3DHoneycomb : public Fill
- clone · function · L15-L15 — Fill* clone() const override { return new Fill3DHoneycomb(*this); };
- use_bridge_flow · function · L20-L20 — bool use_bridge_flow() const override { return false; }
- is_self_crossing · function · L21-L21 — bool is_self_crossing() override { return false; }
- _fill_surface_single · function · L24-L29 — void _fill_surface_single(
