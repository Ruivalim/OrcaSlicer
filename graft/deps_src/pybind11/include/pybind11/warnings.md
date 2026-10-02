# deps_src/pybind11/include/pybind11/warnings.h

- PYBIND11_NAMESPACE_BEGIN · function · L15-L30 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- error_already_set · function · L27-L27 — throw error_already_set();
- PYBIND11_NAMESPACE_BEGIN · function · L34-L34 — PYBIND11_NAMESPACE_BEGIN(warnings)
- new_warning_type · function · L37-L37 — new_warning_type(handle scope, const char *name, handle base = PyExc_RuntimeWarning)
- ptr · function · L38-L38 — if (!detail::PyWarning_Check(base.ptr()))
- PyWarning_Check · function · L38-L38 — if (!detail::PyWarning_Check(base.ptr()))
- h · function · L48-L48 — handle h(PyErr_NewException(full_name.c_str(), base.ptr(), nullptr));
- ptr · function · L48-L48 — handle h(PyErr_NewException(full_name.c_str(), base.ptr(), nullptr));
- error_already_set · function · L52-L52 — throw error_already_set();
- warn · function · L61-L61 — warn(const char *message, handle category = PyExc_RuntimeWarning, int stack_level = 2)
- PYBIND11_NAMESPACE_END · function · L75-L75 — PYBIND11_NAMESPACE_END(PYBIND11_NAMESPACE)
