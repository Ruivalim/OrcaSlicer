# src/libslic3r/Fill/FillCrossHatch.hpp

- FillCrossHatch · class · L12-L26 — class FillCrossHatch : public Fill
- clone · function · L15-L15 — Fill *clone() const override { return new FillCrossHatch(*this); };
- is_self_crossing · function · L17-L17 — bool is_self_crossing() override { return false; }
- _fill_surface_single · function · L20-L25 — void _fill_surface_single(
