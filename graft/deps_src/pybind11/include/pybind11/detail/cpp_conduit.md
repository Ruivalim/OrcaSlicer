# deps_src/pybind11/include/pybind11/detail/cpp_conduit.h

- PYBIND11_NAMESPACE_BEGIN · function · L12-L26 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- pybind11_object_new · function · L16-L16 — extern "C" inline PyObject *pybind11_object_new(PyTypeObject *type, PyObject *, PyObject *);
- type_is_managed_by_our_internals · function · L18-L18 — inline bool type_is_managed_by_our_internals(PyTypeObject *type_obj)
- is_instance_method_of_type · function · L28-L31 — inline bool is_instance_method_of_type(PyTypeObject *type_obj, PyObject *attr_name)
- try_get_cpp_conduit_method · function · L33-L56 — inline object try_get_cpp_conduit_method(PyObject *obj)
- try_raw_pointer_ephemeral_from_cpp_conduit · function · L58-L59 — inline void *try_raw_pointer_ephemeral_from_cpp_conduit(handle src,
- cpp_type_info_capsule · function · L62-L63 — capsule cpp_type_info_capsule(const_cast<void *>(static_cast<const void *>(cpp_type_info)),
- typeid · function · L63-L63 — typeid(std::type_info).name());
- PYBIND11_NAMESPACE_END · function · L75-L75 — PYBIND11_NAMESPACE_END(PYBIND11_NAMESPACE)
