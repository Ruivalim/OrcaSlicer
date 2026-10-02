# tests/catch2/src/catch2/matchers/catch_matchers_exception.hpp

- ExceptionMessageMatcher · class · L16-L27 — class ExceptionMessageMatcher final : public MatcherBase<std::exception>
- ExceptionMessageMatcher · function · L20-L22 — ExceptionMessageMatcher(std::string const& message):
- match · function · L24-L24 — bool match(std::exception const& ex) const override;
- describe · function · L26-L26 — std::string describe() const override;
- Message · function · L30-L30 — ExceptionMessageMatcher Message(std::string const& message);
- ExceptionMessageMatchesMatcher · class · L32-L48 — template <typename StringMatcherType>
- ExceptionMessageMatchesMatcher · function · L38-L39 — ExceptionMessageMatchesMatcher( StringMatcherType matcher ):
- match · function · L41-L43 — bool match( std::exception const& ex ) const override
- describe · function · L45-L47 — std::string describe() const override
- MessageMatches · function · L52-L56 — template <typename StringMatcherType>
