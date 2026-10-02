# src/libslic3r/EmbossShape.hpp

- EmbossProjection · class · L19-L33 — struct EmbossProjection
- serialize · function · L32-L32 — template<class Archive> void serialize(Archive &ar) { ar(depth, use_surface); }
- HealedExPolygons · class · L36-L40 — struct HealedExPolygons
- ExPolygonsWithId · class · L44-L57 — struct ExPolygonsWithId
- EmbossShape · class · L63-L134 — struct EmbossShape
- SvgFile · class · L87-L118 — struct SvgFile
- save · function · L104-L110 — template<class Archive> void save(Archive &ar) const
- load · function · L111-L117 — template<class Archive> void load(Archive &ar)
- save · function · L123-L128 — template<class Archive> void save(Archive &ar) const
- load · function · L129-L133 — template<class Archive> void load(Archive &ar)
- serialize · function · L139-L139 — template<class Archive> void serialize(Archive &ar, Slic3r::ExPolygonsWithId &o) { ar(o.id, o.expoly, o.is_healed); }
- serialize · function · L140-L140 — template<class Archive> void serialize(Archive &ar, Slic3r::HealedExPolygons &o) { ar(o.expolygons, o.is_healed); }
