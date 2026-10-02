# src/libslic3r/CustomGCode.hpp

- DynamicPrintConfig · class · L10-L10 — class DynamicPrintConfig;
- Type · type · L14-L22 — enum Type
- Item · class · L24-L65 — struct Item
- from_json · function · L47-L64 — void from_json(const nlohmann::json& j)
- Mode · type · L67-L75 — enum Mode
- Info · class · L82-L111 — struct Info
- from_json · function · L94-L110 — void from_json(const nlohmann::json& j)
- check_mode_for_custom_gcode_per_print_z · function · L121-L121 — extern void check_mode_for_custom_gcode_per_print_z(Info& info);
- custom_tool_changes · function · L125-L125 — std::vector<std::pair<double, unsigned int>> custom_tool_changes(const Info& custom_gcode_per_print_z, size_t num_extruders);
