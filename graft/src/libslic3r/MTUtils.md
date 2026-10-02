# src/libslic3r/MTUtils.hpp

- SpinMutex · class · L18-L29 — class SpinMutex
- SpinMutex · function · L25-L25 — inline SpinMutex() { m_flg.clear(MO_REL); }
- lock · function · L26-L26 — inline void lock() { while (m_flg.test_and_set(MO_ACQ)) ; }
- try_lock · function · L27-L27 — inline bool try_lock() { return !m_flg.test_and_set(MO_ACQ); }
- unlock · function · L28-L28 — inline void unlock() { m_flg.clear(MO_REL); }
- CachedObject · class · L32-L75 — template<class T> class CachedObject
- CachedObject · function · L49-L52 — template<class... Args>
- invalidate · function · L58-L63 — template<class Fn> void invalidate(Fn &&fn)
- lck · function · L60-L60 — std::lock_guard<SpinMutex> lck(m_lck);
- get · function · L66-L66 — inline const T &get()
- lck · function · L68-L68 — std::lock_guard<SpinMutex> lck(m_lck);
- all_of · function · L77-L84 — template<class C> bool all_of(const C &container)
- linspace_vector · function · L90-L104 — template<class T, class I, class = IntegerOnly<I>>
- vals · function · L95-L95 — std::vector<T> vals(n, T());
- linspace_array · function · L106-L118 — template<size_t N, class T>
- grid · function · L124-L137 — template<class T>
