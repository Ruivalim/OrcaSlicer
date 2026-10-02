# deps_src/pybind11/include/pybind11/detail/value_and_holder.h

- PYBIND11_NAMESPACE_BEGIN · function · L14-L16 — PYBIND11_NAMESPACE_BEGIN(detail)
- value_and_holder · function · L32-L32 — explicit value_and_holder(size_t index) : index{index} {}
- bool · function · L39-L39 — explicit operator bool() const { return value_ptr() != nullptr; }
- holder_constructed · function · L45-L45 — bool holder_constructed() const
- set_holder_constructed · function · L51-L51 — void set_holder_constructed(bool v = true)
- instance_registered · function · L60-L60 — bool instance_registered() const
- set_instance_registered · function · L66-L66 — void set_instance_registered(bool v = true)
- is_holder_constructed · function · L84-L87 — inline bool is_holder_constructed(PyObject *obj)
- PYBIND11_NAMESPACE_END · function · L90-L90 — PYBIND11_NAMESPACE_END(PYBIND11_NAMESPACE)
