# tests/fff_print/test_wipe_tower.cpp

- non_klipper_flavors · function · L19-L26 — static std::vector<GCodeFlavor> non_klipper_flavors()
- flavor_name · function · L28-L31 — static std::string flavor_name(GCodeFlavor flavor)
- wipe_tower_regions · function · L123-L140 — static std::string wipe_tower_regions(const std::string &gcode)
- wipe_tower_toolchange_config · function · L145-L160 — static DynamicPrintConfig wipe_tower_toolchange_config(const std::string &gcode_flavor)
- slice_with_prime_tower · function · L166-L173 — static std::string slice_with_prime_tower(const DynamicPrintConfig &config)
- DYNAMIC_SECTION · function · L180-L185 — DYNAMIC_SECTION(flavor)
- tower_estimate_config · function · L191-L208 — static DynamicPrintConfig tower_estimate_config(const char *wall_type, unsigned int filaments = 2)
