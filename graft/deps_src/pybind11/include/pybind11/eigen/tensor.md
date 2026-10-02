# deps_src/pybind11/include/pybind11/eigen/tensor.h

- PYBIND11_WARNING_DISABLE_MSVC · function · L20-L21 — PYBIND11_WARNING_DISABLE_MSVC(4554)
- static_assert · function · L30-L30 — static_assert(EIGEN_VERSION_AT_LEAST(3, 3, 0),
- PYBIND11_WARNING_DISABLE_MSVC · function · L33-L41 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- is_correct_shape · function · L64-L67 — static constexpr bool
- free · function · L85-L85 — static void free(Type *tensor) { delete tensor; }
- cast · function · L222-L228 — static handle cast(Type &&src, return_value_policy policy, handle parent)
- cast · function · L230-L236 — static handle cast(const Type &&src, return_value_policy policy, handle parent)
- cast · function · L238-L244 — static handle cast(Type &src, return_value_policy policy, handle parent)
- cast · function · L246-L252 — static handle cast(const Type &src, return_value_policy policy, handle parent)
- cast · function · L254-L261 — static handle cast(Type *src, return_value_policy policy, handle parent)
- cast · function · L263-L270 — static handle cast(const Type *src, return_value_policy policy, handle parent)
- load · function · L375-L415 — bool load(handle src, bool /*convert*/)
- cast · function · L417-L419 — static handle cast(MapType &&src, return_value_policy policy, handle parent)
- cast · function · L421-L423 — static handle cast(const MapType &&src, return_value_policy policy, handle parent)
- cast · function · L425-L431 — static handle cast(MapType &src, return_value_policy policy, handle parent)
- cast · function · L433-L439 — static handle cast(const MapType &src, return_value_policy policy, handle parent)
- cast · function · L441-L448 — static handle cast(MapType *src, return_value_policy policy, handle parent)
- cast · function · L450-L457 — static handle cast(const MapType *src, return_value_policy policy, handle parent)
