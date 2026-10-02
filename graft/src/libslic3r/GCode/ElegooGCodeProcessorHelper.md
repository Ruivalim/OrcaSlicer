# src/libslic3r/GCode/ElegooGCodeProcessorHelper.cpp

- equals_case_insensitive · function · L13-L18 — bool equals_case_insensitive(std::string_view lhs, std::string_view rhs)
- get_clamped_param · function · L20-L25 — float get_clamped_param(const GCodeReader::GCodeLine& line, char axis, float default_value, float min_value, float max_value)
- extrusion_time · function · L27-L30 — float extrusion_time(float e_length, float feedrate)
- retract_time · function · L32-L36 — float retract_time(float e_length)
- s819_time · function · L38-L46 — float s819_time(float e_length, float feedrate)
- estimate_M6211_time_for_centauri_carbon · function · L48-L84 — float estimate_M6211_time_for_centauri_carbon(const GCodeReader::GCodeLine& line, float length, double current_x,
- estimate_M6211_time_for_centauri_carbon_2 · function · L86-L121 — float estimate_M6211_time_for_centauri_carbon_2(const GCodeReader::GCodeLine& line, float length, float new_extruder_temp)
- estimate_M6211_time · function · L123-L132 — float estimate_M6211_time(const GCodeReader::GCodeLine& line, std::string_view printer_model, float length, float new_extruder_temp, double current_x, double current_y)
- process_elegoo_M6211 · method · L136-L188 — void GCodeProcessor::process_elegoo_M6211(const GCodeReader::GCodeLine& line)
