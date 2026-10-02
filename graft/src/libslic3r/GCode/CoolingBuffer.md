# src/libslic3r/GCode/CoolingBuffer.hpp

- GCode · class · L11-L11 — class GCode;
- Layer · class · L12-L12 — class Layer;
- CoolingBuffer · class · L24-L61 — class CoolingBuffer
- CoolingBuffer · function · L26-L26 — CoolingBuffer(GCode &gcodegen);
- reset · function · L27-L27 — void        reset(const Vec3d &position);
- set_current_extruder · function · L28-L28 — void        set_current_extruder(unsigned int extruder_id, unsigned int nozzle_id) { m_current_extruder = extruder_id; m_current_nozzle = nozzle_id; }
- process_layer · function · L29-L29 — std::string process_layer(std::string &&gcode, size_t layer_id, bool flush);
- parse_layer_gcode · function · L33-L33 — std::vector<PerExtruderAdjustments> parse_layer_gcode(const std::string &gcode, std::vector<float> &current_pos) const;
- calculate_layer_slowdown · function · L34-L34 — float       calculate_layer_slowdown(std::vector<PerExtruderAdjustments> &per_extruder_adjustments);
- apply_layer_cooldown · function · L37-L37 — std::string apply_layer_cooldown(const std::string &gcode, size_t layer_id, float layer_time, std::vector<PerExtruderAdjustments> &per_extruder_adjustments);
