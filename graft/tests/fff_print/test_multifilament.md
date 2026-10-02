# tests/fff_print/test_multifilament.cpp

- tools_for_role · function · L28-L41 — static std::set<int> tools_for_role(const std::string& gcode, const std::string& role)
- wait_park_xs · function · L45-L66 — static std::vector<double> wait_park_xs(const std::string& gcode)
- stream · function · L48-L48 — std::istringstream stream(gcode);
- elapsed_time_by_line · function · L74-L98 — static std::vector<double> elapsed_time_by_line(const std::string& gcode)
- temperature_trace · function · L108-L167 — static std::vector<std::string> temperature_trace(const std::string& gcode)
- stream · function · L111-L111 — std::istringstream       stream(gcode);
- TraceEntry · class · L178-L183 — struct TraceEntry
- parse_trace_entry · function · L185-L217 — static TraceEntry parse_trace_entry(const std::string& entry)
- timings_match · function · L219-L224 — static bool timings_match(const std::optional<double>& a, const std::optional<double>& b)
- time_is_rounded_lead · function · L227-L232 — static bool time_is_rounded_lead(const TraceEntry& e)
- trace_entries_match · function · L235-L245 — static bool trace_entries_match(const std::string& a, const std::string& b)
- gcode_stream · function · L345-L345 — std::istringstream gcode_stream(gcode);
- gcode_stream · function · L475-L475 — std::istringstream gcode_stream(gcode);
- out · function · L649-L649 — std::ofstream out(golden_path);
- in · function · L663-L663 — std::ifstream in(golden_path);
