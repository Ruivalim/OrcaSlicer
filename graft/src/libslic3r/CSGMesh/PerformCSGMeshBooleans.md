# src/libslic3r/CSGMesh/PerformCSGMeshBooleans.hpp

- BooleanFailReason · type · L14-L14 — enum class BooleanFailReason { OK, MeshEmpty, NotBoundAVolume, SelfIntersect, NoIntersection};
- get_cgalmesh · function · L18-L40 — template<class CSGPartT>
- get_mcutmesh · function · L44-L67 — template<class CSGPartT>
- perform_csg · function · L73-L94 — inline void perform_csg(CSGType op, CGALMeshPtr &dst, CGALMeshPtr &src)
- get_cgalptrs · function · L96-L109 — template<class Ex, class It>
- perform_csg · function · L117-L138 — inline void perform_csg(CSGType op, McutMeshPtr& dst, McutMeshPtr& src)
- get_mcutptrs · function · L140-L153 — template<class Ex, class It>
- perform_csgmesh_booleans_cgal · function · L158-L205 — template<class It>
- Frame · class · L166-L172 — struct Frame
- Frame · function · L168-L171 — explicit Frame(CSGType csgop = CSGType::Union)
- perform_csgmesh_booleans_mcut · function · L208-L256 — template<class It>
- Frame · class · L216-L222 — struct Frame
- Frame · function · L218-L221 — explicit Frame(CSGType csgop = CSGType::Union)
- check_csgmesh_booleans · function · L259-L320 — template<class It, class Visitor>
- check_csgmesh_booleans · function · L322-L359 — template<class It>
- perform_csgmesh_booleans · function · L361-L368 — template<class It>
- perform_csgmesh_booleans_mcut · function · L370-L377 — template<class It>
