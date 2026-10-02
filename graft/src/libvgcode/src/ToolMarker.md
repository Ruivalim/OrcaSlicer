# src/libvgcode/src/ToolMarker.hpp

- ToolMarker · class · L15-L69 — class ToolMarker
- ToolMarker · function · L18-L18 — ToolMarker() = default;
- ToolMarker · function · L20-L20 — ToolMarker(const ToolMarker& other) = delete;
- ToolMarker · function · L21-L21 — ToolMarker(ToolMarker&& other) = delete;
- init · function · L28-L28 — void init(uint16_t resolution, float tip_radius, float tip_height, float stem_radius, float stem_height);
- shutdown · function · L32-L32 — void shutdown();
- render · function · L33-L33 — void render();
- get_position · function · L35-L35 — const Vec3& get_position() const { return m_position; }
- set_position · function · L36-L36 — void set_position(const Vec3& position) { m_position = position; }
- get_offset_z · function · L38-L38 — float get_offset_z() const { return m_offset_z; }
- set_offset_z · function · L39-L39 — void set_offset_z(float offset_z) { m_offset_z = std::max(offset_z, 0.0f); }
- get_color · function · L41-L41 — const Color& get_color() const { return m_color; }
- set_color · function · L42-L42 — void set_color(const Color& color) { m_color = color; }
- get_alpha · function · L44-L44 — float get_alpha() const { return m_alpha; }
- set_alpha · function · L45-L45 — void set_alpha(float alpha) { m_alpha = std::clamp(alpha, 0.25f, 0.75f); }
- size_in_bytes_gpu · function · L50-L50 — size_t size_in_bytes_gpu() const { return m_size_in_bytes_gpu; }
