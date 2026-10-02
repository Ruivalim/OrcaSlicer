# deps_src/pybind11/include/pybind11/detail/function_record_pyobject.h

- PYBIND11_NAMESPACE_BEGIN · function · L18-L103 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- PYBIND11_NAMESPACE_BEGIN · function · L26-L28 — PYBIND11_NAMESPACE_BEGIN(function_record_PyTypeObject_methods)
- tp_new_impl · function · L28-L28 — PyObject *tp_new_impl(PyTypeObject *type, PyObject *args, PyObject *kwds);
- tp_alloc_impl · function · L29-L29 — PyObject *tp_alloc_impl(PyTypeObject *type, Py_ssize_t nitems);
- reduce_ex_impl · function · L34-L34 — static PyObject *reduce_ex_impl(PyObject *self, PyObject *, PyObject *);
- get_function_record_PyTypeObject · function · L93-L93 — inline PyTypeObject *get_function_record_PyTypeObject()
- error_already_set · function · L98-L98 — throw error_already_set();
- is_function_record_PyObject · function · L105-L124 — inline bool is_function_record_PyObject(PyObject *obj)
- function_record_ptr_from_PyObject · function · L126-L126 — inline function_record *function_record_ptr_from_PyObject(PyObject *obj)
- function_record_PyObject_New · function · L133-L140 — inline object function_record_PyObject_New()
- error_already_set · function · L136-L136 — throw error_already_set();
- tp_new_impl · function · L145-L145 — inline PyObject *tp_new_impl(PyTypeObject *, PyObject *, PyObject *)
- tp_alloc_impl · function · L150-L150 — inline PyObject *tp_alloc_impl(PyTypeObject *, Py_ssize_t)
- tp_init_impl · function · L155-L158 — inline int tp_init_impl(PyObject *, PyObject *, PyObject *)
- tp_free_impl · function · L160-L162 — inline void tp_free_impl(void *)
- reduce_ex_impl · function · L164-L164 — inline PyObject *reduce_ex_impl(PyObject *self, PyObject *, PyObject *)
- PYBIND11_NAMESPACE_END · function · L190-L190 — PYBIND11_NAMESPACE_END(detail)
