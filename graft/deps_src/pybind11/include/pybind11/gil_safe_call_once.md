# deps_src/pybind11/include/pybind11/gil_safe_call_once.h

- T · function · L64-L64 — ::new (storage_) T(fn()); // fn may release, but will reacquire, the GIL.
- gil_safe_call_once_and_store · function · L85-L85 — constexpr gil_safe_call_once_and_store() = default;
- gil_safe_call_once_and_store · function · L86-L86 — PYBIND11_DTOR_CONSTEXPR ~gil_safe_call_once_and_store() = default;
