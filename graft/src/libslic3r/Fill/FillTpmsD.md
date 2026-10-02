# src/libslic3r/Fill/FillTpmsD.hpp

- Point · class · L12-L12 — class Point;
- FillTpmsD · class · L14-L42 — class FillTpmsD : public Fill
- FillTpmsD · function · L17-L17 — FillTpmsD() {}
- clone · function · L18-L18 — Fill* clone() const override { return new FillTpmsD(*this); }
- use_bridge_flow · function · L21-L21 — bool use_bridge_flow() const override { return false; }
- _fill_surface_single · function · L28-L32 — void _fill_surface_single(const FillParams&              params,
- is_self_crossing · function · L34-L34 — bool is_self_crossing() override { return false; }
