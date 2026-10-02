# deps_src/nlohmann/detail/iterators/iteration_proxy.hpp

- int_to_string · function · L16-L22 — template<typename string_type>
- iteration_proxy_value · class · L23-L118 — template<typename IteratorType> class iteration_proxy_value
- iteration_proxy_value · function · L46-L48 — explicit iteration_proxy_value(IteratorType it) noexcept
- key · function · L78-L78 — const string_type& key() const
- value · function · L114-L117 — typename IteratorType::reference value() const
- iteration_proxy · class · L121-L143 — template<typename IteratorType> class iteration_proxy
- iteration_proxy · function · L129-L130 — explicit iteration_proxy(typename IteratorType::reference cont) noexcept
- begin · function · L133-L136 — iteration_proxy_value<IteratorType> begin() noexcept
- end · function · L139-L142 — iteration_proxy_value<IteratorType> end() noexcept
- get · function · L147-L151 — template<std::size_t N, typename IteratorType, enable_if_t<N == 0, int> = 0>
- get · function · L155-L159 — template<std::size_t N, typename IteratorType, enable_if_t<N == 1, int> = 0>
