# src/libslic3r/Fill/FillGyroid.hpp

- FillGyroid · class · L10-L38 — class FillGyroid : public Fill
- FillGyroid · function · L13-L13 — FillGyroid() {}
- clone · function · L14-L14 — Fill* clone() const override { return new FillGyroid(*this); }
- use_bridge_flow · function · L17-L17 — bool use_bridge_flow() const override { return false; }
- is_self_crossing · function · L18-L18 — bool is_self_crossing() override { return false; }
- _fill_surface_single · function · L32-L37 — void _fill_surface_single(
