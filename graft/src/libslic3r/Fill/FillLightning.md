# src/libslic3r/Fill/FillLightning.hpp

- PrintObject · class · L8-L8 — class PrintObject;
- Generator · class · L12-L12 — class Generator;
- GeneratorDeleter · class · L14-L14 — struct GeneratorDeleter { void operator()(Generator *p); };
- build_generator · function · L17-L17 — GeneratorPtr build_generator(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- Filler · class · L19-L37 — class Filler : public Slic3r::Fill
- is_self_crossing · function · L23-L23 — bool is_self_crossing() override { return false; }
- clone · function · L27-L27 — Fill* clone() const override { return new Filler(*this); }
- _fill_surface_single · function · L29-L33 — void _fill_surface_single(const FillParams              &params,
- no_sort · function · L36-L36 — bool no_sort() const override { return false; }
