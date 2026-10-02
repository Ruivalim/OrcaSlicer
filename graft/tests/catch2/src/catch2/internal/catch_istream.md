# tests/catch2/src/catch2/internal/catch_istream.hpp

- IStream · class · L19-L35 — class IStream
- stream · function · L22-L22 — virtual std::ostream& stream() = 0;
- isConsole · function · L34-L34 — virtual bool isConsole() const { return false; }
- makeStream · function · L48-L48 — auto makeStream( std::string const& filename ) -> Detail::unique_ptr<IStream>;
