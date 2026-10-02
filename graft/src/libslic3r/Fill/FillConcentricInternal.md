# src/libslic3r/Fill/FillConcentricInternal.hpp

- FillConcentricInternal · class · L8-L20 — class FillConcentricInternal : public Fill
- fill_surface_extrusion · function · L12-L12 — void fill_surface_extrusion(const Surface *surface, const FillParams &params, ExtrusionEntitiesPtr &out) override;
- is_self_crossing · function · L13-L13 — bool is_self_crossing() override { return false; }
- clone · function · L16-L16 — Fill* clone() const override { return new FillConcentricInternal(*this); };
- no_sort · function · L17-L17 — bool no_sort() const override { return true; }
