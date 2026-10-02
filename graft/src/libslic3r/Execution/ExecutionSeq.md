# src/libslic3r/Execution/ExecutionSeq.hpp

- ExecutionSeq · class · L13-L13 — struct ExecutionSeq {};
- IsSequentialEP_ · class · L19-L19 — template<class EP> struct IsSequentialEP_ { static constexpr bool value = false; };
- _Mtx · class · L36-L36 — struct _Mtx { inline void lock() {} inline void unlock() {} };
- lock · function · L36-L36 — struct _Mtx { inline void lock() {} inline void unlock() {} };
- unlock · function · L36-L36 — struct _Mtx { inline void lock() {} inline void unlock() {} };
- loop_ · function · L38-L42 — template<class Fn, class It>
- loop_ · function · L44-L48 — template<class Fn, class I>
- for_each · function · L54-L62 — template<class It, class Fn>
- reduce · function · L64-L77 — template<class I, class MergeFn, class T, class AccessFn>
- max_concurrency · function · L79-L79 — static size_t max_concurrency(const EP &) { return 1; }
