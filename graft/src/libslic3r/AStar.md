# src/libslic3r/AStar.hpp

- TracerTraits_ · class · L17-L39 — template<class T> struct TracerTraits_
- foreach_reachable · function · L24-L24 — template<class Fn> static void foreach_reachable(const T &tracer, const Node &src, Fn &&fn) { tracer.foreach_reachable(src, fn); }
- distance · function · L28-L28 — static float distance(const T &tracer, const Node &a, const Node &b) { return tracer.distance(a, b); }
- goal_heuristic · function · L35-L35 — static float goal_heuristic(const T &tracer, const Node &n) { return tracer.goal_heuristic(n); }
- unique_id · function · L38-L38 — static size_t unique_id(const T &tracer, const Node &n) { return tracer.unique_id(n); }
- QNode · class · L46-L58 — template<class Tracer> struct QNode // Queue node. Keeps track of scores g, and h
- f · function · L53-L53 — float f() const { return g + h; }
- QNode · function · L55-L57 — QNode(TracerNodeT<Tracer> n = {}, size_t p = Unassigned, float gval = std::numeric_limits<float>::infinity(), float hval = 0.f)
- search_route · function · L74-L153 — template<class Tracer, class It, class NodeMap = std::unordered_map<size_t, QNode<Tracer>>>
- LessPred · class · L81-L85 — struct LessPred
