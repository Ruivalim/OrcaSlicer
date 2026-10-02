# src/libvgcode/src/ExtrusionRoles.hpp

- ExtrusionRoles · class · L14-L32 — class ExtrusionRoles
- Item · class · L17-L20 — struct Item
- add · function · L22-L22 — void add(EGCodeExtrusionRole role, const std::array<float, TIME_MODES_COUNT>& times);
- get_roles_count · function · L24-L24 — std::size_t get_roles_count() const { return m_items.size(); }
- get_roles · function · L25-L25 — std::vector<EGCodeExtrusionRole> get_roles() const;
- get_time · function · L26-L26 — float get_time(EGCodeExtrusionRole role, ETimeMode mode) const;
- reset · function · L28-L28 — void reset() { m_items.clear(); }
