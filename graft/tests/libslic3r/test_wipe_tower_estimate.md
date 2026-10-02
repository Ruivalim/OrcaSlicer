# tests/libslic3r/test_wipe_tower_estimate.cpp

- preset_shaped_defaults · function · L22-L27 — static DynamicPrintConfig preset_shaped_defaults()
- make_config · function · L29-L50 — static DynamicPrintConfig make_config(const char *wall_type = "rectangle")
- filaments · function · L52-L57 — static std::vector<unsigned int> filaments(size_t count)
- ids · function · L54-L54 — std::vector<unsigned int> ids(count);
- estimate · function · L60-L63 — static WipeTowerFootprint estimate(const ConfigBase &config, size_t count, double layer_height, double height, WipeTowerType type = WipeTowerType::Type2)
- printed_brim · function · L66-L69 — static double printed_brim(double configured, WipeTowerType type)
