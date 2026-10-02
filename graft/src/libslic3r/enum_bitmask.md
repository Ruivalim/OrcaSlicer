# src/libslic3r/enum_bitmask.hpp

- enum_bitmask · class · L13-L56 — template<class option_type, typename = typename std::enable_if<std::is_enum<option_type>::value>::type>
- mask_value · function · L19-L19 — static constexpr underlying_type mask_value(option_type o) { return 1 << static_cast<underlying_type>(o); }
- enum_bitmask · function · L22-L22 — explicit constexpr enum_bitmask(underlying_type o) : m_bits(o) {}
- enum_bitmask · function · L26-L26 — constexpr enum_bitmask() : m_bits(0) {}
- enum_bitmask · function · L31-L31 — constexpr enum_bitmask(option_type o) : m_bits(mask_value(o)) {}
- has · function · L47-L47 — constexpr bool has(option_type t) const { return m_bits & mask_value(t); }
- lower · function · L52-L52 — constexpr bool lower(const enum_bitmask r) const { return m_bits < r.m_bits; }
- is_enum_bitmask_type · class · L59-L59 — template<typename Enum> struct is_enum_bitmask_type { static const bool enable = false; };
- only_if · function · L77-L81 — template <class option_type>
- only_if · function · L83-L87 — template <class option_type>
