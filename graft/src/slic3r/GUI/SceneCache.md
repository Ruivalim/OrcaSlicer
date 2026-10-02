# src/slic3r/GUI/SceneCache.hpp

- GLModel · class · L11-L11 — class GLModel;
- SceneCache · class · L14-L53 — class SceneCache
- Key · class · L18-L37 — struct Key
- capture · function · L40-L40 — void capture(Key key);
- matches · function · L41-L41 — bool matches(const Key& key) const { return m_valid && m_key == key; }
- render · function · L43-L43 — void render(GLModel& quad);
- invalidate · function · L44-L44 — void invalidate() { m_valid = false; }
- reset · function · L46-L46 — void reset();
