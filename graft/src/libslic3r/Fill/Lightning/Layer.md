# src/libslic3r/Fill/Lightning/Layer.hpp

- Node · class · L19-L19 — class Node;
- GroundingLocation · class · L23-L28 — struct GroundingLocation
- p · function · L27-L27 — Point p() const;
- Layer · class · L35-L88 — class Layer
- generateNewTrees · function · L40-L49 — void generateNewTrees
- getBestGroundingLocation · function · L54-L64 — GroundingLocation getBestGroundingLocation
- attach · function · L71-L71 — bool attach(const Point& unsupported_location, const GroundingLocation& ground, NodeSPtr& new_child, NodeSPtr& new_root);
- reconnectRoots · function · L73-L81 — void reconnectRoots
- convertToLines · function · L83-L83 — Polylines convertToLines(const Polygons& limit_to_outline, coord_t line_overlap) const;
- getWeightedDistance · function · L85-L85 — coord_t getWeightedDistance(const Point& boundary_loc, const Point& unsupported_location);
- fillLocator · function · L87-L87 — void fillLocator(SparseNodeGrid& tree_node_locator, const BoundingBox& current_outlines_bbox);
