# src/slic3r/GUI/DeviceCore/DevMapping.h

- MappingOption · type · L13-L19 — enum MappingOption
- is_valid_mapping_result · function · L28-L28 — static bool is_valid_mapping_result(const MachineObject* obj, std::vector<FilamentInfo>& result, bool check_empty_slot = false);
- ams_filament_mapping · function · L30-L30 — static int ams_filament_mapping(const MachineObject* obj, const std::vector<FilamentInfo>& filaments, std::vector<FilamentInfo>& result, std::vector<bool> map_opt, std::vector<int> exclude_id = std::vector<int>(), bool nozzle_has_ams_then_ignore_ext = false);
