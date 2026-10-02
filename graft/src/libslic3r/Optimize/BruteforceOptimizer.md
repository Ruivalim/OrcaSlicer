# src/libslic3r/Optimize/BruteforceOptimizer.hpp

- num_iter · function · L12-L18 — template<size_t N>
- AlgBurteForce · class · L23-L103 — struct AlgBurteForce
- AlgBurteForce · function · L28-L28 — AlgBurteForce(const StopCriteria &cr, size_t gs): stc{cr}, gridsz{gs} {}
- run · function · L35-L80 — template<int D, size_t N, class Fn, class Cmp>
- optimize · function · L82-L102 — template<class Fn, size_t N>
- Optimizer · function · L115-L117 — Optimizer(const StopCriteria &cr = {}, size_t gridsz = 100)
- to_max · function · L119-L119 — Optimizer& to_max() { m_alg.to_min = false; return *this; }
- to_min · function · L120-L120 — Optimizer& to_min() { m_alg.to_min = true;  return *this; }
- optimize · function · L122-L128 — template<class Func, size_t N>
- set_criteria · function · L130-L130 — Optimizer &set_criteria(const StopCriteria &cr)
- get_criteria · function · L135-L135 — const StopCriteria &get_criteria() const { return m_alg.stc; }
