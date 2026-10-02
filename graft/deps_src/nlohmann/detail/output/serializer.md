# deps_src/nlohmann/detail/output/serializer.hpp

- error_handler_t · type · L32-L37 — enum class error_handler_t
- serializer · class · L39-L582 — template<typename BasicJsonType>
- serializer · function · L56-L65 — serializer(output_adapter_t<char> s, const char ichar,
- serializer · function · L68-L68 — serializer(const serializer&) = delete;
- serializer · function · L70-L70 — serializer(serializer&&) = delete;
- dump · function · L96-L363 — void dump(const BasicJsonType& val,
- for · function · L390-L390 — for (std::size_t i = 0; i < s.size(); ++i)
- switch · function · L394-L578 — switch (decode(state, codepoint, byte))
- count_digits · function · L641-L641 — inline unsigned int count_digits(number_unsigned_t x) noexcept
- dump_integer · function · L676-L758 — template < typename NumberType, detail::enable_if_t <
- dump_float · function · L768-L787 — void dump_float(number_float_t x)
- dump_float · function · L789-L795 — void dump_float(number_float_t x, std::true_type /*is_ieee_single_or_double*/)
- dump_float · function · L797-L846 — void dump_float(number_float_t x, std::false_type /*is_ieee_single_or_double*/)
- decode · function · L869-L902 — static std::uint8_t decode(std::uint8_t& state, std::uint32_t& codep, const std::uint8_t byte) noexcept
- remove_sign · function · L909-L913 — number_unsigned_t remove_sign(number_unsigned_t x)
- remove_sign · function · L924-L928 — inline number_unsigned_t remove_sign(number_integer_t x) noexcept
