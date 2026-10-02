# tests/catch2/src/catch2/internal/catch_string_manip.hpp

- startsWith · function · L21-L21 — bool startsWith( std::string const& s, std::string const& prefix );
- startsWith · function · L22-L22 — bool startsWith( StringRef s, char prefix );
- endsWith · function · L23-L23 — bool endsWith( std::string const& s, std::string const& suffix );
- endsWith · function · L24-L24 — bool endsWith( std::string const& s, char suffix );
- contains · function · L25-L25 — bool contains( std::string const& s, std::string const& infix );
- toLowerInPlace · function · L26-L26 — void toLowerInPlace( std::string& s );
- toLower · function · L27-L27 — std::string toLower( std::string const& s );
- toLower · function · L28-L28 — char toLower( char c );
- trim · function · L30-L30 — std::string trim( std::string const& str );
- trim · function · L32-L32 — StringRef trim( StringRef ref CATCH_ATTR_LIFETIMEBOUND );
- splitStringRef · function · L35-L35 — std::vector<StringRef> splitStringRef( StringRef str CATCH_ATTR_LIFETIMEBOUND, char delimiter );
- replaceInPlace · function · L36-L36 — bool replaceInPlace( std::string& str, std::string const& replaceThis, std::string const& withThis );
- pluralise · class · L48-L59 — class pluralise
- pluralise · function · L53-L56 — constexpr pluralise(std::uint64_t count, StringRef label CATCH_ATTR_LIFETIMEBOUND):
