# deps_src/libnest2d/tools/benchmark.h

- Clock · type · L27-L27 — typedef std::chrono::high_resolution_clock Clock;
- Duration · type · L28-L28 — typedef Clock::duration Duration;
- TimePoint · type · L29-L29 — typedef Clock::time_point TimePoint;
- to_sec · function · L34-L36 — inline double to_sec(Duration d)
- start · function · L43-L43 — void start() {  t1 = Clock::now(); }
- stop · function · L48-L48 — void stop() {  t2 = Clock::now(); }
- getElapsedSec · function · L54-L54 — double getElapsedSec() {  d = t2 - t1; return to_sec(d); }
