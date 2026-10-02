# deps_src/libnest2d/include/libnest2d/selections/djd_heuristic.hpp

- _DJDHeuristic · class · L17-L712 — template<class RawShape>
- SpinLock · class · L21-L32 — class SpinLock
- SpinLock · function · L25-L25 — inline SpinLock(std::atomic_flag& flg): lck_(flg) {}
- lock · function · L27-L29 — inline void lock()
- unlock · function · L31-L31 — inline void unlock() { lck_.clear(std::memory_order_release); }
- Config · class · L41-L91 — struct Config
- configure · function · L106-L108 — inline void configure(const Config& config)
- packItems · function · L110-L711 — template<class TPlacer, class TIterator,
- slock · function · L557-L557 — SpinLock slock(flg);
- not_packeds · function · L654-L654 — std::vector<ItemList> not_packeds(bincount_guess);
- rets · function · L673-L673 — std::vector<std::future<void>> rets(bincount_guess);
