# src/libslic3r/AnyPtr.hpp

- AnyPtr · class · L19-L126 — template<class T>
- get_ptr · function · L25-L25 — template<class Self> static T *get_ptr(Self &&s)
- AnyPtr · function · L41-L43 — template<class TT = T, class = std::enable_if_t<std::is_convertible_v<TT, T>>>
- AnyPtr · function · L44-L46 — template<class TT, class = std::enable_if_t<std::is_convertible_v<TT, T>>>
- AnyPtr · function · L47-L49 — template<class TT, class = std::enable_if_t<std::is_convertible_v<TT, T>>>
- AnyPtr · function · L50-L52 — template<class TT, class = std::enable_if_t<std::is_convertible_v<TT, T>>>
- AnyPtr · function · L56-L56 — AnyPtr(AnyPtr &&other) noexcept : ptr{std::move(other.ptr)} {}
- AnyPtr · function · L57-L57 — AnyPtr(const AnyPtr &other) = delete;
- get · function · L80-L80 — T *get() { return get_ptr(*this); }
- get · function · L81-L81 — const T *get() const { return get_ptr(*this); }
- get_shared_cpy · function · L100-L112 — std::shared_ptr<T> get_shared_cpy() const
- convert_unique_to_shared · function · L115-L119 — void convert_unique_to_shared()
- is_owned · function · L122-L125 — bool is_owned() const noexcept
