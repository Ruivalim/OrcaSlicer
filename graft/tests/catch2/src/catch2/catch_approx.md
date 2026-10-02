# tests/catch2/src/catch2/catch_approx.hpp

- Approx · class · L17-L114 — class Approx
- equalityComparisonImpl · function · L19-L19 — bool equalityComparisonImpl(double other) const;
- setMargin · function · L21-L21 — void setMargin(double margin);
- setEpsilon · function · L23-L23 — void setEpsilon(double epsilon);
- Approx · function · L26-L26 — explicit Approx ( double value );
- custom · function · L28-L28 — static Approx custom();
- approx · function · L34-L34 — Approx approx( static_cast<double>(value) );
- Approx · function · L41-L43 — template <typename T, typename = std::enable_if_t<std::is_constructible<double, T>::value>>
- epsilon · function · L88-L88 — Approx& epsilon( T const& newEpsilon )
- margin · function · L95-L95 — Approx& margin( T const& newMargin )
- scale · function · L102-L102 — Approx& scale( T const& newScale )
- toString · function · L107-L107 — std::string toString() const;
- convert · function · L123-L123 — static std::string convert(Catch::Approx const& value);
