# deps_src/nlohmann/detail/iterators/json_reverse_iterator.hpp

- json_reverse_iterator · class · L33-L117 — template<typename Base>
- json_reverse_iterator · function · L44-L45 — explicit json_reverse_iterator(const typename base_iterator::iterator_type& it) noexcept
- json_reverse_iterator · function · L48-L48 — explicit json_reverse_iterator(const base_iterator& it) noexcept : base_iterator(it) {}
- key · function · L105-L109 — auto key() const -> decltype(std::declval<Base>().key())
- value · function · L112-L116 — reference value() const
