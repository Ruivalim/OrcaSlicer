# src/libslic3r/Execution/Execution.hpp

- IsExecutionPolicy_ · class · L14-L14 — template<class EP> struct IsExecutionPolicy_ : public std::false_type {};
- Traits · class · L26-L26 — template<class EP, class En = void> struct Traits {};
- max_concurrency · function · L36-L40 — template<class EP, class = ExecutionPolicyOnly<EP> >
- for_each · function · L44-L48 — template<class EP, class It, class Fn, class = ExecutionPolicyOnly<EP>>
- reduce · function · L54-L72 — template<class EP,
- reduce · function · L76-L91 — template<class EP,
- accumulate · function · L93-L107 — template<class EP,
- accumulate · function · L110-L123 — template<class EP,
