# src/libslic3r/Timer.hpp

- Timer · class · L13-L28 — class Timer
- Timer · function · L22-L22 — Timer(const std::string& name);
- nanoseconds_since_epoch · function · L33-L35 — static inline uint64_t nanoseconds_since_epoch()
- Timer · class · L38-L57 — class Timer
- start · function · L40-L42 — void start()
- elapsed_nanoseconds · function · L43-L45 — uint64_t elapsed_nanoseconds() const
- elapsed_microseconds · function · L46-L48 — uint64_t elapsed_microseconds() const
- elapsed_milliseconds · function · L49-L51 — unsigned int elapsed_milliseconds() const
- elapsed_seconds · function · L52-L54 — double elapsed_seconds() const
- TimeLimitAlarm · class · L60-L86 — class TimeLimitAlarm
- TimeLimitAlarm · function · L62-L65 — TimeLimitAlarm(uint64_t time_limit_nanoseconds, std::string_view limit_exceeded_message) :
- new_nanos · function · L71-L73 — static TimeLimitAlarm new_nanos(uint64_t time_limit_nanoseconds, std::string_view limit_exceeded_message)
- new_millis · function · L74-L76 — static TimeLimitAlarm new_millis(uint64_t time_limit_millis, std::string_view limit_exceeded_message)
- new_seconds · function · L77-L79 — static TimeLimitAlarm new_seconds(uint64_t time_limit_seconds, std::string_view limit_exceeded_message)
- report_time_exceeded · function · L81-L81 — void report_time_exceeded() const;
