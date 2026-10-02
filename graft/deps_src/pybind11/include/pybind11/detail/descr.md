# deps_src/pybind11/include/pybind11/detail/descr.h

- PYBIND11_NAMESPACE_BEGIN · function · L15-L15 — PYBIND11_NAMESPACE_BEGIN(detail)
- descr · function · L30-L30 — constexpr descr(char const (&s)[N + 1]) : descr(s, make_index_sequence<N>()) {}
- typeid · function · L37-L40 — constexpr descr(char c, Chars... cs) : text{c, static_cast<char>(cs)..., '\0'} {}
- types · function · L39-L39 — static constexpr std::array<const std::type_info *, sizeof...(Ts) + 1> types()
- PYBIND11_WORKAROUND_INCORRECT_MSVC_C4100 · function · L44-L49 — template <size_t N1, size_t N2, typename... Ts1, typename... Ts2, size_t... Is1, size_t... Is2>
- plus_impl · function · L45-L48 — constexpr descr<N1 + N2, Ts1..., Ts2...> plus_impl(const descr<N1, Ts1...> &a,
- plus_impl · function · L54-L56 — constexpr descr<N1 + N2, Ts1..., Ts2...> operator+(const descr<N1, Ts1...> &a,
- const_name · function · L63-L63 — constexpr descr<0> const_name(char const (&)[1]) { return {}; }
- io_name · function · L116-L119 — template <bool B, size_t N1, size_t N2, size_t N3, size_t N4>
- io_name · function · L118-L118 — io_name(char const (&)[N1], char const (&)[N2], char const (&text3)[N3], char const (&text4)[N4])
- concat · function · L159-L159 — constexpr descr<0> concat() { return {}; }
- union_concat · function · L160-L160 — constexpr descr<0> union_concat() { return {}; }
- decltype · function · L197-L200 — constexpr auto concat(const descr<N, Ts...> &d, const Args &...args)
- decltype · function · L203-L206 — constexpr auto union_concat(const descr<N, Ts...> &d, const Args &...args)
- PYBIND11_NAMESPACE_END · function · L226-L226 — PYBIND11_NAMESPACE_END(PYBIND11_NAMESPACE)
