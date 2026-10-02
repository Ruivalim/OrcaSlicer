# src/slic3r/GUI/TickCode.hpp

- TickCode · class · L12-L22 — struct TickCode
- TickCodeInfo · class · L24-L58 — class TickCodeInfo
- get_color_for_tick · function · L33-L33 — std::string get_color_for_tick(TickCode tick, Type type, const int extruder);
- empty · function · L39-L39 — bool empty() const { return ticks.empty(); }
- set_pause_print_msg · function · L40-L40 — void set_pause_print_msg(const std::string& message) { pause_print_msg = message; }
- add_tick · function · L42-L42 — bool add_tick(const int tick, Type type, int extruder, double print_z);
- edit_tick · function · L43-L43 — bool edit_tick(std::set<TickCode>::iterator it, double print_z);
- switch_code · function · L44-L44 — void switch_code(Type type_from, Type type_to);
- switch_code_for_tick · function · L45-L45 — bool switch_code_for_tick(std::set<TickCode>::iterator it, Type type_to, const int extruder);
- erase_all_ticks_with_code · function · L46-L46 — void erase_all_ticks_with_code(Type type);
- has_tick_with_code · function · L48-L48 — bool            has_tick_with_code(Type type);
- has_tick · function · L49-L49 — bool            has_tick(int tick);
- suppress_plus · function · L51-L51 — void suppress_plus(bool suppress) { m_suppress_plus = suppress; }
- suppress_minus · function · L52-L52 — void suppress_minus(bool suppress) { m_suppress_minus = suppress; }
- suppressed_plus · function · L53-L53 — bool suppressed_plus() { return m_suppress_plus; }
- suppressed_minus · function · L54-L54 — bool suppressed_minus() { return m_suppress_minus; }
- set_default_colors · function · L55-L55 — void set_default_colors(bool default_colors_on) { m_use_default_colors = default_colors_on; }
- set_extruder_colors · function · L57-L57 — void set_extruder_colors(std::vector<std::string>* extruder_colors) { m_colors = extruder_colors; }
