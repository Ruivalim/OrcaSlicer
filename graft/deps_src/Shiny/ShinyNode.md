# deps_src/Shiny/ShinyNode.h

- _ShinyNode · class · L37-L55 — typedef struct _ShinyNode
- ShinyNode_addChild · function · L65-L74 — SHINY_INLINE void ShinyNode_addChild(ShinyNode* self,  ShinyNode* a_child)
- ShinyNode_init · function · L76-L86 — SHINY_INLINE void ShinyNode_init(ShinyNode* self, ShinyNode* a_parent, struct _ShinyZone* a_zone, ShinyNodeCache* a_cache)
- ShinyNode_updateTree · function · L88-L88 — SHINY_API void ShinyNode_updateTree(ShinyNode* self, float a_damping);
- ShinyNode_updateTreeClean · function · L89-L89 — SHINY_API void ShinyNode_updateTreeClean(ShinyNode* self);
- ShinyNode_destroy · function · L91-L93 — SHINY_INLINE void ShinyNode_destroy(ShinyNode* self)
- ShinyNode_appendTicks · function · L95-L97 — SHINY_INLINE void ShinyNode_appendTicks(ShinyNode* self, shinytick_t a_elapsedTicks)
- ShinyNode_beginEntry · function · L99-L101 — SHINY_INLINE void ShinyNode_beginEntry(ShinyNode* self)
- ShinyNode_isRoot · function · L103-L105 — SHINY_INLINE int ShinyNode_isRoot(ShinyNode* self)
- ShinyNode_isDummy · function · L107-L109 — SHINY_INLINE int ShinyNode_isDummy(ShinyNode* self)
- ShinyNode_isEqual · function · L111-L113 — SHINY_INLINE int ShinyNode_isEqual(ShinyNode* self, const ShinyNode* a_parent, const struct _ShinyZone* a_zone)
- ShinyNode_findNextInTree · function · L115-L115 — SHINY_API const ShinyNode* ShinyNode_findNextInTree(const ShinyNode* self);
- ShinyNode_clear · function · L117-L117 — SHINY_API void ShinyNode_clear(ShinyNode* self);
- ShinyNode_enumerateNodes · function · L119-L119 — SHINY_API void ShinyNode_enumerateNodes(const ShinyNode* a_node, void (*a_func)(const ShinyNode*));
- void · function · L125-L125 — void ShinyNode_enumerateNodes(const ShinyNode* a_node, T* a_this, void (T::*a_func)(const ShinyNode*))
