# src/libslic3r/Time.hpp

- get_current_time_utc · function · L11-L11 — time_t get_current_time_utc();
- TimeZone · type · L13-L13 — enum class TimeZone { local, utc };
- TimeFormat · type · L14-L14 — enum class TimeFormat { gcode, iso8601Z };
- time2str · function · L18-L18 — std::string time2str(const time_t &t, TimeZone zone, TimeFormat fmt);
- time2str · function · L20-L23 — inline std::string time2str(TimeZone zone, TimeFormat fmt)
- utc_timestamp · function · L25-L28 — inline std::string utc_timestamp(time_t t)
- utc_timestamp · function · L30-L33 — inline std::string utc_timestamp()
- local_timestamp · function · L35-L37 — inline std::string local_timestamp(TimeFormat fmt = TimeFormat::gcode)
- str2time · function · L40-L40 — time_t str2time(const std::string &str, TimeZone zone, TimeFormat fmt);
- iso_utc_timestamp · function · L51-L54 — inline std::string iso_utc_timestamp(time_t t)
- iso_utc_timestamp · function · L56-L59 — inline std::string iso_utc_timestamp()
- parse_iso_utc_timestamp · function · L61-L64 — inline time_t parse_iso_utc_timestamp(const std::string &str)
- millis_to_iso8601 · function · L72-L72 — std::string millis_to_iso8601(long long unix_millis);
- iso8601_to_millis · function · L73-L73 — long long iso8601_to_millis(const std::string& iso_time);  // Returns -1 on parse error
