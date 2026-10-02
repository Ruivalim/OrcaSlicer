# src/libvgcode/src/ViewRange.hpp

- ViewRange · class · L12-L52 — class ViewRange
- get_full · function · L15-L15 — const Interval& get_full() const { return m_full.get(); }
- set_full · function · L16-L16 — void set_full(const Range& other) { set_full(other.get()); }
- set_full · function · L17-L17 — void set_full(const Interval& range) { set_full(range[0], range[1]); }
- set_full · function · L18-L18 — void set_full(Interval::value_type min, Interval::value_type max);
- get_enabled · function · L20-L20 — const Interval& get_enabled() const { return m_enabled.get(); }
- set_enabled · function · L21-L21 — void set_enabled(const Range& other) { set_enabled(other.get()); }
- set_enabled · function · L22-L22 — void set_enabled(const Interval& range) { set_enabled(range[0], range[1]); }
- set_enabled · function · L23-L23 — void set_enabled(Interval::value_type min, Interval::value_type max);
- get_visible · function · L25-L25 — const Interval& get_visible() const { return m_visible.get(); }
- set_visible · function · L26-L26 — void set_visible(const Range& other) { set_visible(other.get()); }
- set_visible · function · L27-L27 — void set_visible(const Interval& range) { set_visible(range[0], range[1]); }
- set_visible · function · L28-L28 — void set_visible(Interval::value_type min, Interval::value_type max);
- reset · function · L30-L30 — void reset();
