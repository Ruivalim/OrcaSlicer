# deps_src/nlohmann/detail/iterators/iter_impl.hpp

- iteration_proxy · class · L19-L19 — template<typename IteratorType> class iteration_proxy;
- iteration_proxy_value · class · L20-L20 — template<typename IteratorType> class iteration_proxy_value;
- iter_impl · class · L38-L262 — template<typename BasicJsonType>
- iter_impl · function · L78-L78 — iter_impl() = default;
- iter_impl · function · L80-L80 — iter_impl(iter_impl&&) noexcept = default;
- iter_impl · function · L89-L121 — explicit iter_impl(pointer object) noexcept : m_object(object)
- iter_impl · function · L139-L141 — iter_impl(const iter_impl<const BasicJsonType>& other) noexcept
- iter_impl · function · L164-L166 — iter_impl(const iter_impl<typename std::remove_const<BasicJsonType>::type>& other) noexcept
- key · function · L711-L711 — const typename object_t::key_type& key() const
- value · function · L727-L730 — reference value() const
