# deps_src/libnest2d/include/libnest2d/selections/selection_boilerplate.hpp

- SelectionBoilerplate · class · L9-L64 — template<class RawShape>
- getResult · function · L17-L17 — inline const PackGroup& getResult() const
- lastPackedBinId · function · L21-L21 — inline int lastPackedBinId() const { return last_packed_bin_id_; }
- progressIndicator · function · L23-L23 — inline void progressIndicator(ProgressFunction fn) { progress_ = fn; }
- stopCondition · function · L25-L25 — inline void stopCondition(StopCondition cond) { stopcond_ = cond; }
- unfitIndicator · function · L27-L27 — inline void unfitIndicator(UnfitIndicator fn) { unfitindicator_ = fn; }
- clear · function · L29-L29 — inline void clear() { packed_bins_.clear(); }
- remove_unpackable_items · function · L33-L57 — template<class Placer, class Container, class Bin, class PCfg>
