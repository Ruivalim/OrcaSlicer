# src/libslic3r/Fill/FillSpiralInset.hpp

- FillSpiralInset · class · L8-L33 — class FillSpiralInset : public Fill
- is_self_crossing · function · L12-L12 — bool is_self_crossing() override { return false; }
- clone · function · L15-L15 — Fill* clone() const override { return new FillSpiralInset(*this); };
- _fill_surface_single · function · L16-L21 — void _fill_surface_single(
- _fill_surface_single · function · L25-L30 — void _fill_surface_single(
- no_sort · function · L32-L32 — bool no_sort() const override { return true; }
