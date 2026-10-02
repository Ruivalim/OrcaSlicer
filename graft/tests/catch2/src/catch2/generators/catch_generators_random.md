# tests/catch2/src/catch2/generators/catch_generators_random.hpp

- getSeed · function · L23-L23 — std::uint32_t getSeed();
- RandomFloatingGenerator · class · L26-L45 — template <typename Float>
- RandomFloatingGenerator · function · L32-L36 — RandomFloatingGenerator( Float a, Float b, std::uint32_t seed ):
- get · function · L38-L38 — Float const& get() const override
- next · function · L41-L44 — bool next() override
- RandomFloatingGenerator · function · L56-L56 — RandomFloatingGenerator( long double a, long double b, std::uint32_t seed );
- get · function · L58-L58 — long double const& get() const override { return m_current_number; }
- next · function · L59-L59 — bool next() override;
- RandomIntegerGenerator · class · L64-L83 — template <typename Integer>
- RandomIntegerGenerator · function · L70-L74 — RandomIntegerGenerator( Integer a, Integer b, std::uint32_t seed ):
- get · function · L76-L76 — Integer const& get() const override
- next · function · L79-L82 — bool next() override
- random · function · L85-L91 — template <typename T>
- random · function · L93-L100 — template <typename T>
