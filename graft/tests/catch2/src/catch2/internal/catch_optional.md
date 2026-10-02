# tests/catch2/src/catch2/internal/catch_optional.hpp

- Optional · class · L18-L113 — template<typename T>
- Optional · function · L21-L21 — Optional(): nullableValue( nullptr ) {}
- Optional · function · L24-L25 — Optional( T const& _value ):
- Optional · function · L26-L27 — Optional( T&& _value ):
- Optional · function · L40-L41 — Optional( Optional const& _other ):
- Optional · function · L42-L44 — Optional( Optional&& _other ):
- reset · function · L63-L66 — void reset()
- valueOr · function · L85-L87 — T valueOr( T const& defaultValue ) const
- some · function · L89-L89 — bool some() const { return nullableValue != nullptr; }
- none · function · L90-L90 — bool none() const { return nullableValue == nullptr; }
