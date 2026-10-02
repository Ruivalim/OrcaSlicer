# src/libvgcode/src/Layers.hpp

- Layers · class · L14-L56 — class Layers
- update · function · L17-L17 — void update(const PathVertex& vertex, uint32_t vertex_id);
- reset · function · L18-L18 — void reset();
- empty · function · L20-L20 — bool empty() const { return m_items.empty(); }
- count · function · L21-L21 — std::size_t count() const { return m_items.size(); }
- get_times · function · L23-L23 — std::vector<float> get_times(ETimeMode mode) const;
- get_zs · function · L24-L24 — std::vector<float> get_zs() const;
- get_layer_time · function · L26-L29 — float get_layer_time(ETimeMode mode, std::size_t layer_id) const
- get_layer_z · function · L30-L32 — float get_layer_z(std::size_t layer_id) const
- get_layer_id_at · function · L33-L33 — std::size_t get_layer_id_at(float z) const;
- get_view_range · function · L35-L35 — const Interval& get_view_range() const { return m_view_range.get(); }
- set_view_range · function · L36-L36 — void set_view_range(const Interval& range) { set_view_range(range[0], range[1]); }
- set_view_range · function · L37-L37 — void set_view_range(Interval::value_type min, Interval::value_type max) { m_view_range.set(min, max); }
- layer_contains_colorprint_options · function · L39-L41 — bool layer_contains_colorprint_options(std::size_t layer_id) const
- size_in_bytes_cpu · function · L43-L43 — std::size_t size_in_bytes_cpu() const;
- Item · class · L46-L52 — struct Item
