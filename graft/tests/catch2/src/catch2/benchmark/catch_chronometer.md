# tests/catch2/src/catch2/benchmark/catch_chronometer.hpp

- ChronometerConcept · class · L21-L29 — struct ChronometerConcept
- start · function · L22-L22 — virtual void start() = 0;
- finish · function · L23-L23 — virtual void finish() = 0;
- ChronometerConcept · function · L26-L26 — ChronometerConcept() = default;
- ChronometerConcept · function · L27-L27 — ChronometerConcept(ChronometerConcept const&) = default;
- ChronometerModel · class · L30-L42 — template <typename Clock>
- start · function · L32-L32 — void start() override { started = Clock::now(); }
- finish · function · L33-L33 — void finish() override { finished = Clock::now(); }
- elapsed · function · L35-L38 — IDuration elapsed() const
- Chronometer · class · L45-L73 — struct Chronometer
- measure · function · L47-L48 — template <typename Fun>
- runs · function · L50-L50 — int runs() const { return repeats; }
- Chronometer · function · L52-L54 — Chronometer(Detail::ChronometerConcept& meter, int repeats_)
- measure · function · L57-L60 — template <typename Fun>
- measure · function · L62-L69 — template <typename Fun>
