# src/libvgcode/include/ColorRange.hpp

- ColorRange · class · L28-L103 — class ColorRange
- ColorRange · function · L34-L34 — explicit ColorRange(EColorRangeType type = EColorRangeType::Linear);
- get_type · function · L38-L38 — EColorRangeType get_type() const;
- get_palette · function · L43-L43 — const Palette& get_palette() const;
- set_palette · function · L48-L48 — void set_palette(const Palette& palette);
- get_color_at · function · L53-L53 — Color get_color_at(float value) const;
- get_range · function · L60-L60 — const std::array<float, 2>& get_range() const;
- get_values · function · L68-L68 — std::vector<float> get_values() const;
- size_in_bytes_cpu · function · L72-L72 — std::size_t size_in_bytes_cpu() const;
- update · function · L95-L95 — void update(float value);
- reset · function · L100-L100 — void reset();
