# tests/catch2/src/catch2/benchmark/detail/catch_benchmark_function.hpp

- BenchmarkFunction · class · L33-L82 — struct BenchmarkFunction
- callable · class · L35-L42 — struct callable
- call · function · L36-L36 — virtual void call(Chronometer meter) const = 0;
- callable · function · L39-L39 — callable() = default;
- callable · function · L40-L40 — callable(callable&&) = default;
- model · class · L43-L59 — template <typename Fun>
- model · function · L45-L45 — model(Fun&& fun_) : fun(CATCH_MOVE(fun_)) {}
- model · function · L46-L46 — model(Fun const& fun_) : fun(fun_) {}
- call · function · L48-L50 — void call(Chronometer meter) const override
- call · function · L51-L53 — void call(Chronometer meter, std::true_type) const
- call · function · L54-L56 — void call(Chronometer meter, std::false_type) const
- BenchmarkFunction · function · L62-L62 — BenchmarkFunction();
- BenchmarkFunction · function · L64-L67 — template <typename Fun,
- BenchmarkFunction · function · L69-L70 — BenchmarkFunction( BenchmarkFunction&& that ) noexcept:
