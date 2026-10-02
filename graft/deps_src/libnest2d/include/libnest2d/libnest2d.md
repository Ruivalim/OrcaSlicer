# deps_src/libnest2d/include/libnest2d/libnest2d.hpp

- NestConfig · class · L64-L77 — template<class Placer = NfpPlacer, class Selector = FirstFitSelection>
- NestConfig · function · L71-L71 — NestConfig() = default;
- NestConfig · function · L72-L72 — NestConfig(const typename Placer::Config &cfg)   : placer_config{cfg} {}
- NestConfig · function · L73-L73 — NestConfig(const typename Selector::Config &cfg) : selector_config{cfg} {}
- NestConfig · function · L74-L76 — NestConfig(const typename Placer::Config &  pcfg,
- NestControl · class · L79-L89 — struct NestControl
- NestControl · function · L83-L83 — NestControl() = default;
- NestControl · function · L84-L84 — NestControl(ProgressFunction pr) : progressfn{std::move(pr)} {}
- NestControl · function · L85-L85 — NestControl(StopCondition sc) : stopcond{std::move(sc)} {}
- NestControl · function · L86-L88 — NestControl(ProgressFunction pr, StopCondition sc)
- nest · function · L91-L104 — template<class Placer = NfpPlacer,
- nest · function · L108-L115 — extern template class _Nester<NfpPlacer, FirstFitSelection>;
- nest · function · L116-L121 — extern template std::size_t nest(std::vector<Item>::iterator from,
- nest · function · L125-L135 — template<class Placer = NfpPlacer,
- mm · function · L137-L140 — template<class T = double> enable_if_t<std::is_arithmetic<T>::value, TCoord<PointImpl>> mm(T val = T(1))
