# deps_src/pybind11/include/pybind11/subinterpreter.h

- PYBIND11_NAMESPACE_BEGIN · function · L22-L53 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- get_interpreter_state_unchecked · function · L24-L24 — inline PyInterpreterState *get_interpreter_state_unchecked()
- subinterpreter_scoped_activate · function · L40-L40 — explicit subinterpreter_scoped_activate(subinterpreter const &si);
- create · function · L79-L127 — static inline subinterpreter create(PyInterpreterConfig const &cfg)
- main_guard · function · L85-L85 — subinterpreter_scoped_activate main_guard(main());
- PyThreadState_Get · function · L87-L87 — auto prev_tstate = PyThreadState_Get();
- create · function · L131-L139 — static inline subinterpreter create()
- main · function · L200-L205 — static subinterpreter main()
- current · function · L208-L213 — static subinterpreter current()
- id · function · L216-L216 — int64_t id() const
- state_dict · function · L225-L225 — dict state_dict() { return reinterpret_borrow<dict>(PyInterpreterState_GetDict(istate_)); }
- disarm · function · L229-L229 — void disarm() { creation_tstate_ = nullptr; }
- empty · function · L232-L232 — bool empty() const { return istate_ == nullptr; }
- bool · function · L235-L235 — explicit operator bool() const { return !empty(); }
- scope_ · function · L247-L248 — explicit scoped_subinterpreter(PyInterpreterConfig const &cfg)
- scoped_subinterpreter · function · L247-L248 — explicit scoped_subinterpreter(PyInterpreterConfig const &cfg)
- subinterpreter_scoped_activate · function · L255-L276 — inline subinterpreter_scoped_activate::subinterpreter_scoped_activate(subinterpreter const &si)
- subinterpreter_scoped_activate · function · L278-L297 — inline subinterpreter_scoped_activate::~subinterpreter_scoped_activate()
