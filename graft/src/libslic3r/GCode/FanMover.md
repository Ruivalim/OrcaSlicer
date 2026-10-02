# src/libslic3r/GCode/FanMover.hpp

- BufferData · class · L16-L28 — class BufferData
- BufferData · function · L24-L27 — BufferData(std::string line, float time = 0, int16_t fan_speed = 0, float is_kickstart = false) : raw(line), time(time), fan_speed(fan_speed), is_kickstart(is_kickstart)
- FanMover · class · L30-L93 — class FanMover
- FanMover · function · L64-L71 — FanMover(const GCodeWriter& writer, const float nb_seconds_delay, const bool with_D_option, const bool relative_e,
- process_gcode · function · L74-L74 — const std::string& process_gcode(const std::string& gcode, bool flush);
- put_in_buffer · function · L77-L77 — BufferData& put_in_buffer(BufferData&& data)
- remove_from_buffer · function · L82-L85 — std::list<BufferData>::iterator remove_from_buffer(std::list<BufferData>::iterator data)
- _process_gcode_line · function · L87-L87 — void _process_gcode_line(GCodeReader& reader, const GCodeReader::GCodeLine& line);
- _process_T · function · L88-L88 — void _process_T(const std::string_view command);
- _put_in_middle_G1 · function · L89-L89 — void _put_in_middle_G1(std::list<BufferData>::iterator item_to_split, float nb_sec, BufferData&& line_to_write);
- _print_in_middle_G1 · function · L90-L90 — void _print_in_middle_G1(BufferData& line_to_split, float nb_sec, const std::string& line_to_write);
- _remove_slow_fan · function · L91-L91 — void _remove_slow_fan(int16_t min_speed, float past_sec);
- _set_fan · function · L92-L92 — std::string _set_fan(int16_t speed);
