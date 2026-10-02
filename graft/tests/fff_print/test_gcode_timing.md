# tests/fff_print/test_gcode_timing.cpp

- make_config · function · L31-L43 — FullPrintConfig make_config(double load_time, double unload_time, double tool_change_time)
- run_processor · function · L45-L59 — void run_processor(GCodeProcessor& proc, const FullPrintConfig& config, const char* gcode)
- role_times · function · L64-L71 — std::map<ExtrusionRole, double> role_times(const GCodeProcessorResult& r)
- sum_tool_change_time · function · L74-L81 — double sum_tool_change_time(const GCodeProcessorResult& r)
- filament_change_delay · function · L84-L88 — double filament_change_delay(const GCodeProcessorResult& r)
- make_junction_config · function · L435-L466 — FullPrintConfig make_junction_config(GCodeFlavor flavor, double corner_velocity, double junction_deviation)
- corner_gcode · function · L475-L493 — std::string corner_gcode(double turn_deg, double orientation_deg, double e_per_mm = 0.0)
- corner_speed · function · L497-L505 — double corner_speed(const GCodeProcessorResult& r)
- planned_corner_speed · function · L507-L514 — double planned_corner_speed(GCodeFlavor flavor, double corner_velocity, double junction_deviation,
