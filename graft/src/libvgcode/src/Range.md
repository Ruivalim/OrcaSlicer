# src/libvgcode/src/Range.hpp

- Range · class · L12-L35 — class Range
- get · function · L15-L15 — const Interval& get() const { return m_range; }
- set · function · L16-L16 — void set(const Range& other) { m_range = other.m_range; }
- set · function · L17-L17 — void set(const Interval& range) { set(range[0], range[1]); }
- set · function · L18-L18 — void set(Interval::value_type min, Interval::value_type max);
- get_min · function · L20-L20 — Interval::value_type get_min() const { return m_range[0]; }
- set_min · function · L21-L21 — void set_min(Interval::value_type min) { set(min, m_range[1]); }
- get_max · function · L23-L23 — Interval::value_type get_max() const { return m_range[1]; }
- set_max · function · L24-L24 — void set_max(Interval::value_type max) { set(m_range[0], max); }
- clamp · function · L27-L27 — void clamp(Range& other);
- reset · function · L28-L28 — void reset() { m_range = { 0, 0 }; }
