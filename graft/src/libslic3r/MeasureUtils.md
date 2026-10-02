# src/libslic3r/MeasureUtils.hpp

- Polynomial1 · class · L13-L92 — class Polynomial1
- Polynomial1 · function · L16-L24 — Polynomial1(std::initializer_list<double> values)
- Polynomial1 · function · L33-L35 — explicit Polynomial1(uint32_t degree)
- EliminateLeadingZeros · function · L46-L59 — void EliminateLeadingZeros()
- SetCoefficients · function · L62-L65 — void SetCoefficients(double value)
- GetDegree · function · L67-L71 — inline uint32_t GetDegree() const
- result · function · L114-L114 — Polynomial1 result(p0Degree);
- result · function · L125-L125 — Polynomial1 result(p1Degree);
- result · function · L143-L143 — Polynomial1 result(p0Degree);
- result · function · L154-L154 — Polynomial1 result(p1Degree);
- result · function · L169-L169 — Polynomial1 result(degree);
- RootsPolynomial · class · L180-L346 — class RootsPolynomial
- Find · function · L188-L222 — static int32_t Find(int32_t degree, const double* c, uint32_t maxIterations, double* roots)
- Find · function · L226-L271 — static bool Find(int32_t degree, const double* c, double tmin, double tmax, uint32_t maxIterations, double& root)
- FindRecursive · function · L274-L335 — static int32_t FindRecursive(int32_t degree, double const* c, double tmin, double tmax, uint32_t maxIterations, double* roots)
- derivRoots · function · L307-L307 — std::vector<double> derivRoots(derivDegree);
- Evaluate · function · L337-L345 — static double Evaluate(int32_t degree, const double* c, double t)
- get_orthogonal · function · L355-L381 — inline Vec3d get_orthogonal(const Vec3d& v, bool unitLength)
