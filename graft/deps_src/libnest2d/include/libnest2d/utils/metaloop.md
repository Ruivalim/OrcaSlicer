# deps_src/libnest2d/include/libnest2d/utils/metaloop.hpp

- index_sequence · class · L17-L20 — template<size_t...Ints> struct index_sequence
- size · function · L19-L19 — BP2D_CONSTEXPR value_type size() const { return sizeof...(Ints); }
- metaloop · class · L58-L223 — class metaloop
- MapFn · class · L84-L99 — template<int N, class Fn> class MapFn
- MapFn · function · L92-L92 — inline MapFn(Fn&& fn): fn_(forward<Fn>(fn)) {}
- _MetaLoop · class · L108-L109 — template <typename Idx, class...Args>
- run · function · L119-L122 — template<class Tup, class Fn>
- run · function · L132-L139 — template<class Tup, class Fn>
- apply · function · L188-L192 — template<class...Args, class Fn>
- apply · function · L195-L198 — template<class...Args, class Fn>
- apply · function · L201-L204 — template<class...Args, class Fn>
- apply · function · L207-L210 — template<class...Args, class Fn>
- callFunWithTuple · function · L215-L221 — template<class Fn, class Tup, std::size_t...Is>
