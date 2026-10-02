# deps_src/pybind11/include/pybind11/embed.h

- PYBIND11_NAMESPACE_BEGIN · function · L65-L82 — PYBIND11_WARNING_POP
- init_t · function · L73-L74 — embedded_module(const char *name, init_t init)
- PyImport_AppendInittab · function · L78-L78 — auto result = PyImport_AppendInittab(name, init);
- wide_char_arg_deleter · class · L85-L89 — struct wide_char_arg_deleter
- widen_chars · function · L92-L92 — inline wchar_t *widen_chars(const char *safe_arg)
- precheck_interpreter · function · L97-L101 — inline void precheck_interpreter()
- initialize_interpreter_pre_pyconfig · function · L108-L133 — inline void initialize_interpreter_pre_pyconfig(bool init_signal_handlers,
- initialize_interpreter · function · L139-L140 — inline void initialize_interpreter(PyConfig *config,
- initialize_interpreter · function · L187-L187 — inline void initialize_interpreter(bool init_signal_handlers = true,
- finalize_interpreter · function · L243-L270 — inline void finalize_interpreter()
- scoped_interpreter · function · L289-L289 — explicit scoped_interpreter(bool init_signal_handlers = true,
- scoped_interpreter · function · L297-L298 — explicit scoped_interpreter(PyConfig *config,
