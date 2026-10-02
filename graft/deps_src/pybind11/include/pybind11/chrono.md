# deps_src/pybind11/include/pybind11/chrono.h

- PYBIND11_NAMESPACE_BEGIN · function · L21-L59 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- load · function · L33-L33 — bool load(handle src, bool)
- get_duration · function · L63-L63 — get_duration(const std::chrono::duration<rep, period> &src)
- get_duration · function · L67-L67 — get_duration(const std::chrono::duration<rep, period> &&)
- cast · function · L77-L100 — static handle cast(const type &src, return_value_policy /* policy */, handle /* parent */)
- get_duration · function · L82-L82 — auto d = get_duration(src);
- localtime_thread_safe · function · L105-L105 — inline std::tm *localtime_thread_safe(const std::time_t *time, std::tm *buf)
- load · function · L126-L174 — bool load(handle src, bool)
- cast · function · L176-L212 — static handle cast(const std::chrono::time_point<std::chrono::system_clock, Duration> &src,
