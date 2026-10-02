# src/libslic3r/MaterialType.hpp

- MaterialTypeInfo · class · L8-L17 — struct MaterialTypeInfo
- MaterialType · class · L19-L30 — class MaterialType
- all · function · L21-L21 — static const std::vector<MaterialTypeInfo>& all();
- find · function · L23-L23 — static const MaterialTypeInfo* find(const std::string& name);
- get_temperature_range · function · L25-L25 — static bool get_temperature_range(const std::string& type, int& min_temp, int& max_temp);
- get_chamber_temperature_range · function · L26-L26 — static bool get_chamber_temperature_range(const std::string& type, int& chamber_min_temp, int& chamber_max_temp);
- get_adhesion_coefficient · function · L27-L27 — static bool get_adhesion_coefficient(const std::string& type, double& adhesion_coefficient);
- get_yield_strength · function · L28-L28 — static bool get_yield_strength(const std::string& type, double& yield_strength);
- get_thermal_length · function · L29-L29 — static bool get_thermal_length(const std::string& type, double& thermal_length);
