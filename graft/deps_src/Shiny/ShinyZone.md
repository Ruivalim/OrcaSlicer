# deps_src/Shiny/ShinyZone.h

- _ShinyZone · class · L44-L49 — typedef struct _ShinyZone
- ShinyZone_init · function · L54-L57 — SHINY_INLINE void ShinyZone_init(ShinyZone *self, ShinyZone* a_prev)
- ShinyZone_uninit · function · L59-L62 — SHINY_INLINE void ShinyZone_uninit(ShinyZone *self)
- ShinyZone_preUpdateChain · function · L64-L64 — SHINY_API void ShinyZone_preUpdateChain(ShinyZone *first);
- ShinyZone_updateChain · function · L65-L65 — SHINY_API void ShinyZone_updateChain(ShinyZone *first, float a_damping);
- ShinyZone_updateChainClean · function · L66-L66 — SHINY_API void ShinyZone_updateChainClean(ShinyZone *first);
- ShinyZone_resetChain · function · L68-L68 — SHINY_API void ShinyZone_resetChain(ShinyZone *first);
- ShinyZone_compare · function · L72-L74 — SHINY_INLINE float ShinyZone_compare(ShinyZone *a, ShinyZone *b)
- ShinyZone_clear · function · L76-L76 — SHINY_API void ShinyZone_clear(ShinyZone* self);
- ShinyZone_enumerateZones · function · L78-L78 — SHINY_API void ShinyZone_enumerateZones(const ShinyZone* a_zone, void (*a_func)(const ShinyZone*));
- void · function · L84-L84 — void ShinyZone_enumerateZones(const ShinyZone* a_zone, T* a_this, void (T::*a_func)(const ShinyZone*))
