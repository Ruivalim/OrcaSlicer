# src/libslic3r/Fill/Lightning/Generator.hpp

- PrintObject · class · L15-L15 — class PrintObject;
- Generator · class · L37-L133 — class Generator  // "Just like Nicola used to make!"
- Generator · function · L47-L47 — explicit Generator(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- getTreesForLayer · function · L58-L58 — const Layer& getTreesForLayer(const size_t& layer_id) const;
- Overhangs · function · L60-L60 — std::vector<Polygons>& Overhangs() { return m_overhang_per_layer; }
- infilll_extrusion_width · function · L62-L62 — float infilll_extrusion_width() const { return m_infill_extrusion_width; }
- Generator · function · L64-L64 — Generator(PrintObject* m_object, std::vector<Polygons>& contours, std::vector<Polygons>& overhangs, const std::function<void()> &throw_on_cancel_callback, float density = 0.15);
- generateInitialInternalOverhangs · function · L75-L75 — void generateInitialInternalOverhangs(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- generateTrees · function · L80-L80 — void generateTrees(const PrintObject &print_object, const std::function<void()> &throw_on_cancel_callback);
- generateTreesforSupport · function · L81-L81 — void generateTreesforSupport(std::vector<Polygons>& contours, const std::function<void()> &throw_on_cancel_callback);
