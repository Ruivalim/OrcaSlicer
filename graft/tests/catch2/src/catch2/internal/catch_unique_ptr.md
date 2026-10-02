# tests/catch2/src/catch2/internal/catch_unique_ptr.hpp

- unique_ptr · class · L23-L103 — template <typename T>
- unique_ptr · function · L27-L29 — constexpr unique_ptr(std::nullptr_t = nullptr):
- unique_ptr · function · L30-L32 — explicit constexpr unique_ptr(T* ptr):
- unique_ptr · function · L34-L37 — template <typename U, typename = std::enable_if_t<std::is_base_of<T, U>::value>>
- unique_ptr · function · L46-L46 — unique_ptr(unique_ptr const&) = delete;
- unique_ptr · function · L49-L52 — unique_ptr(unique_ptr&& rhs) noexcept:
- get · function · L80-L80 — T* get() { return m_ptr; }
- get · function · L81-L81 — T const* get() const { return m_ptr; }
- reset · function · L83-L86 — void reset(T* ptr = nullptr)
- release · function · L88-L88 — T* release()
- swap · function · L98-L102 — friend void swap(unique_ptr& lhs, unique_ptr& rhs)
- make_unique · function · L109-L112 — template <typename T, typename... Args>
