# src/libslic3r/Channel.hpp

- Channel · class · L15-L96 — template<class T> class Channel
- Unlocker · class · L20-L32 — template<class Ptr> class Unlocker
- Unlocker · function · L23-L23 — Unlocker(UniqueLock lock) : m_lock(std::move(lock)) {}
- Unlocker · function · L24-L24 — Unlocker(const Unlocker &other) noexcept : m_lock(std::move(other.m_lock)) {}     // XXX: done beacuse of MSVC 2013 not supporting init of deleter by move
- Unlocker · function · L25-L25 — Unlocker(Unlocker &&other) noexcept : m_lock(std::move(other.m_lock)) {}
- Channel · function · L38-L38 — Channel() {}
- push · function · L41-L48 — void push(const T& item, bool silent = false)
- lock · function · L44-L44 — UniqueLock lock(m_mutex);
- push · function · L50-L57 — void push(T &&item, bool silent = false)
- lock · function · L53-L53 — UniqueLock lock(m_mutex);
- pop · function · L59-L66 — T pop()
- lock · function · L61-L61 — UniqueLock lock(m_mutex);
- try_pop · function · L68-L78 — boost::optional<T> try_pop()
- lock · function · L70-L70 — UniqueLock lock(m_mutex);
- size_hint · function · L81-L81 — size_t size_hint() const noexcept { return m_queue.size(); }
- lock_read · function · L83-L86 — LockedConstPtr lock_read() const
- lock_rw · function · L88-L91 — LockedPtr lock_rw()
