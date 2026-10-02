# tests/catch2/src/catch2/internal/catch_stringref.hpp

- StringRef · class · L24-L114 — class StringRef
- StringRef · function · L38-L38 — constexpr StringRef() noexcept = default;
- StringRef · function · L40-L40 — StringRef( char const* rawChars CATCH_ATTR_LIFETIMEBOUND ) noexcept;
- StringRef · function · L42-L46 — constexpr StringRef( char const* rawChars CATCH_ATTR_LIFETIMEBOUND,
- StringRef · function · L48-L52 — StringRef(
- empty · function · L75-L77 — constexpr auto empty() const noexcept -> bool
- size · function · L78-L80 — constexpr auto size() const noexcept -> size_type
- substr · function · L85-L92 — constexpr StringRef substr(size_type start, size_type length) const noexcept
- data · function · L95-L95 — constexpr char const* data() const noexcept CATCH_ATTR_LIFETIMEBOUND
- begin · function · L99-L99 — constexpr const_iterator begin() const { return m_start; }
- end · function · L100-L100 — constexpr const_iterator end() const { return m_start + m_size; }
- compare · function · L113-L113 — int compare( StringRef rhs ) const;
