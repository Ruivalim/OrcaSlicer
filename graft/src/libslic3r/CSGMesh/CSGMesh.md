# src/libslic3r/CSGMesh/CSGMesh.hpp

- CSGType · type · L20-L20 — enum class CSGType { Union, Difference, Intersection };
- CSGStackOp · type · L38-L38 — enum class CSGStackOp { Push, Continue, Pop };
- get_operation · function · L41-L44 — template<class CSGPartT> CSGType get_operation(const CSGPartT &part)
- get_stack_operation · function · L47-L50 — template<class CSGPartT> CSGStackOp get_stack_operation(const CSGPartT &part)
- get_mesh · function · L54-L54 — const indexed_triangle_set *get_mesh(const CSGPartT &part)
- get_transform · function · L61-L65 — template<class CSGPartT>
- CSGPart · class · L68-L83 — struct CSGPart
- CSGPart · function · L75-L82 — CSGPart(AnyPtr<const indexed_triangle_set> ptr = {},
- is_all_positive · function · L87-L97 — template<class Cont> bool is_all_positive(const Cont &csgmesh)
- csgmesh_merge_positive_parts · function · L102-L117 — template<class Cont>
