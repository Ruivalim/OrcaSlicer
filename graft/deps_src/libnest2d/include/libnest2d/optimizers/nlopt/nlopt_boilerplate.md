# deps_src/libnest2d/include/libnest2d/optimizers/nlopt/nlopt_boilerplate.hpp

- method2nloptAlg · function · L22-L30 — inline nlopt::algorithm method2nloptAlg(Method m)
- NloptOptimizer · class · L37-L194 — class NloptOptimizer: public Optimizer<NloptOptimizer>
- BoundsFunc · class · L54-L63 — struct BoundsFunc
- BoundsFunc · function · L56-L56 — inline explicit BoundsFunc(NloptOptimizer& o): self(o) {}
- InitValFunc · class · L65-L73 — struct InitValFunc
- InitValFunc · function · L67-L67 — inline explicit InitValFunc(NloptOptimizer& o): self(o) {}
- ResultCopyFunc · class · L75-L83 — struct ResultCopyFunc
- ResultCopyFunc · function · L77-L77 — inline explicit ResultCopyFunc(NloptOptimizer& o): self(o) {}
- FunvalCopyFunc · class · L85-L94 — struct FunvalCopyFunc
- FunvalCopyFunc · function · L88-L88 — inline explicit FunvalCopyFunc(D& p): params(p) {}
- optfunc · function · L98-L119 — template<class Fn, class...Args>
- optimize · function · L121-L187 — template<class Func, class...Args>
- NloptOptimizer · function · L190-L192 — inline explicit NloptOptimizer(nlopt::algorithm alg,
