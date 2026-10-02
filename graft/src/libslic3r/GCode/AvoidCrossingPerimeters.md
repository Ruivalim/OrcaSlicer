# src/libslic3r/GCode/AvoidCrossingPerimeters.hpp

- GCode · class · L11-L11 — class GCode;
- Layer · class · L12-L12 — class Layer;
- Point · class · L13-L13 — class Point;
- AvoidCrossingPerimeters · class · L15-L71 — class AvoidCrossingPerimeters
- use_external_mp · function · L19-L19 — void        use_external_mp(bool use = true) { m_use_external_mp = use; };
- used_external_mp · function · L20-L20 — bool        used_external_mp() { return m_use_external_mp; }
- use_external_mp_once · function · L21-L21 — void        use_external_mp_once()  { m_use_external_mp_once = true; }
- used_external_mp_once · function · L22-L22 — bool        used_external_mp_once() { return m_use_external_mp_once; }
- disable_once · function · L23-L23 — void        disable_once()          { m_disabled_once = true; }
- disabled_once · function · L24-L24 — bool        disabled_once() const   { return m_disabled_once; }
- reset_once_modifiers · function · L25-L25 — void        reset_once_modifiers()  { m_use_external_mp_once = false; m_disabled_once = false; }
- init_layer · function · L27-L27 — void        init_layer(const Layer &layer);
- travel_to · function · L29-L33 — Polyline    travel_to(const GCode& gcodegen, const Point& point)
- travel_to · function · L35-L35 — Polyline    travel_to(const GCode& gcodegen, const Point& point, bool* could_be_wipe_disabled);
- Boundary · class · L37-L52 — struct Boundary
- clear · function · L47-L51 — void clear()
