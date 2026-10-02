# src/libslic3r/GCode/WipeTowerEstimate.hpp

- ConfigBase · class · L9-L9 — class ConfigBase;
- WipeTowerType · type · L10-L10 — enum class WipeTowerType;
- WipeTowerFootprint · class · L15-L21 — struct WipeTowerFootprint
- resolve_wipe_tower_type · function · L26-L26 — WipeTowerType resolve_wipe_tower_type(const ConfigBase &config);
- estimate_wipe_tower_first_layer_outline · function · L32-L32 — Polygon estimate_wipe_tower_first_layer_outline(const ConfigBase &config, WipeTowerType tower_type, double width, double depth, double height);
- estimate_wipe_tower_footprint · function · L41-L45 — WipeTowerFootprint estimate_wipe_tower_footprint(const ConfigBase                &config,
