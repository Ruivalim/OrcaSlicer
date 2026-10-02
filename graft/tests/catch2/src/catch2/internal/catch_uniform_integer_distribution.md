# tests/catch2/src/catch2/internal/catch_uniform_integer_distribution.hpp

- uniform_integer_distribution · class · L27-L104 — template <typename IntegerType>
- computeDistance · function · L51-L55 — static constexpr UnsignedIntegerType computeDistance(IntegerType a, IntegerType b)
- computeRejectionThreshold · function · L57-L62 — static constexpr UnsignedIntegerType computeRejectionThreshold(UnsignedIntegerType ab_distance)
- transposeTo · function · L64-L67 — static constexpr UnsignedIntegerType transposeTo(IntegerType in)
- transposeBack · function · L68-L71 — static constexpr IntegerType transposeBack(UnsignedIntegerType in)
- uniform_integer_distribution · function · L76-L81 — constexpr uniform_integer_distribution( IntegerType a, IntegerType b ):
- a · function · L102-L102 — constexpr result_type a() const { return transposeBack(m_a); }
- b · function · L103-L103 — constexpr result_type b() const { return transposeBack(m_ab_distance + m_a - 1); }
