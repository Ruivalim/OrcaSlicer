# src/libslic3r/Fill/FillConcentric.hpp

- FillConcentric · class · L8-L30 — class FillConcentric : public Fill
- is_self_crossing · function · L12-L12 — bool is_self_crossing() override { return false; }
- clone · function · L15-L15 — Fill* clone() const override { return new FillConcentric(*this); };
- _fill_surface_single · function · L16-L21 — void _fill_surface_single(
- _fill_surface_single · function · L23-L27 — void _fill_surface_single(const FillParams& params,
- no_sort · function · L29-L29 — bool no_sort() const override { return true; }
