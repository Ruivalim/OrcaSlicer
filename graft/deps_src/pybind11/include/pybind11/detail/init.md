# deps_src/pybind11/include/pybind11/detail/init.h

- PYBIND11_WARNING_DISABLE_MSVC · function · L15-L27 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- load · function · L24-L24 — bool load(handle h, bool)
- init_smart_holder_from_unique_ptr · function · L229-L230 — auto smhldr = init_smart_holder_from_unique_ptr(
- move · function · L230-L230 — std::move(unq_ptr), /*void_cast_raw_ptr*/ Class::has_alias && is_alias<Class>(ptr));
- init_smart_holder_from_unique_ptr · function · L243-L244 — auto smhldr
- move · function · L244-L244 — = init_smart_holder_from_unique_ptr(std::move(unq_ptr), /*void_cast_raw_ptr*/ true);
- from_shared_ptr · function · L263-L264 — auto smhldr
- move · function · L264-L264 — = smart_holder::from_shared_ptr(std::const_pointer_cast<Cpp<Class>>(std::move(shd_ptr)));
- from_shared_ptr · function · L287-L287 — auto smhldr = smart_holder::from_shared_ptr(shd_ptr);
- error_already_set · function · L485-L485 — throw error_already_set();
- get · function · L511-L515 — pickle_factory(Get get, Set set) : get(std::forward<Get>(get)), set(std::forward<Set>(set)) {}
- set · function · L511-L513 — pickle_factory(Get get, Set set) : get(std::forward<Get>(get)), set(std::forward<Set>(set)) {}
- execute · function · L514-L515 — void execute(Class &cl, const Extra &...extra) &&
- PYBIND11_NAMESPACE_END · function · L537-L537 — PYBIND11_NAMESPACE_END(detail)
