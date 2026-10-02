# deps_src/nlohmann/ordered_map.hpp

- ordered_map · class · L19-L188 — template <class Key, class T, class IgnoredLess = std::less<Key>,
- ordered_map · function · L33-L33 — ordered_map(const Allocator& alloc = Allocator()) : Container{alloc} {}
- ordered_map · function · L34-L36 — template <class It>
- ordered_map · function · L37-L38 — ordered_map(std::initializer_list<T> init, const Allocator& alloc = Allocator() )
- emplace · function · L40-L51 — std::pair<iterator, bool> emplace(const key_type& key, T&& t)
- at · function · L63-L63 — T& at(const Key& key)
- at · function · L76-L76 — const T& at(const Key& key) const
- erase · function · L89-L106 — size_type erase(const Key& key)
- erase · function · L108-L120 — iterator erase(iterator pos)
- count · function · L122-L132 — size_type count(const Key& key) const
- find · function · L134-L144 — iterator find(const Key& key)
- find · function · L146-L156 — const_iterator find(const Key& key) const
- insert · function · L158-L161 — std::pair<iterator, bool> insert( value_type&& value )
- insert · function · L163-L174 — std::pair<iterator, bool> insert( const value_type& value )
- insert · function · L180-L187 — template<typename InputIt, typename = require_input_iter<InputIt>>
