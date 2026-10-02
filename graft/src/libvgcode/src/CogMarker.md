# src/libvgcode/src/CogMarker.hpp

- CogMarker · class · L12-L71 — class CogMarker
- CogMarker · function · L15-L15 — CogMarker() = default;
- CogMarker · function · L17-L17 — CogMarker(const CogMarker& other) = delete;
- CogMarker · function · L18-L18 — CogMarker(CogMarker&& other) = delete;
- init · function · L25-L25 — void init(uint8_t resolution, float radius);
- shutdown · function · L29-L29 — void shutdown();
- render · function · L33-L33 — void render();
- update · function · L37-L37 — void update(const Vec3& position, float mass);
- reset · function · L41-L41 — void reset();
- get_position · function · L45-L45 — Vec3 get_position() const;
- size_in_bytes_gpu · function · L49-L49 — size_t size_in_bytes_gpu() const { return m_size_in_bytes_gpu; }
