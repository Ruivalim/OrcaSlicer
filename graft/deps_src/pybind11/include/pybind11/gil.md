# deps_src/pybind11/include/pybind11/gil.h

- PYBIND11_NAMESPACE_BEGIN · function · L31-L80 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- PYBIND11_WARNING_DISABLE_GCC · function · L36-L39 — PYBIND11_WARNING_DISABLE_GCC("-Wredundant-decls")
- get_thread_state_unchecked · function · L39-L39 — PyThreadState *get_thread_state_unchecked();
- PYBIND11_NAMESPACE_END · function · L43-L67 — PYBIND11_NAMESPACE_END(detail)
- inc_ref · function · L105-L105 — void inc_ref() { ++tstate->gilstate_counter; }
- dec_ref · function · L107-L130 — PYBIND11_NOINLINE void dec_ref()
- disarm · function · L137-L137 — PYBIND11_NOINLINE void disarm() { active = false; }
- gil_scoped_acquire · function · L139-L144 — PYBIND11_NOINLINE ~gil_scoped_acquire()
- gil_scoped_release · function · L155-L155 — explicit gil_scoped_release(bool disassoc = false) : disassoc(disassoc)
- disarm · function · L176-L176 — PYBIND11_NOINLINE void disarm() { active = false; }
