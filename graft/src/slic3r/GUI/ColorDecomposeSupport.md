# src/slic3r/GUI/ColorDecomposeSupport.hpp

- wxWindow · class · L10-L10 — class wxWindow;
- Preset · class · L13-L13 — class Preset;
- DecomposeOfficialComponent · class · L28-L32 — struct DecomposeOfficialComponent
- DecomposeMissingComponent · class · L34-L39 — struct DecomposeMissingComponent
- decompose_normalize_color_hex · function · L45-L45 — std::string decompose_normalize_color_hex(std::string color);
- decompose_base_color_en · function · L47-L47 — const char* decompose_base_color_en(DecomposeBaseColor color);
- decompose_base_color_display · function · L49-L49 — wxString decompose_base_color_display(DecomposeBaseColor color);
- decompose_basic_type_from_source · function · L51-L53 — std::string decompose_basic_type_from_source(size_t source_config_idx,
- decompose_basic_filament_id · function · L55-L55 — std::string decompose_basic_filament_id(const std::string& basic_type);
- set_created_standard_component_metadata · function · L57-L57 — void set_created_standard_component_metadata(size_t config_idx, const DecomposeOfficialComponent& component);
- lookup_decompose_official_component · function · L59-L62 — DecomposeOfficialComponent lookup_decompose_official_component(
- find_decompose_standard_preset_name · function · L64-L64 — std::string find_decompose_standard_preset_name(size_t source_config_idx, const std::string& basic_type);
- official_basic_type_from_preset_name · function · L68-L68 — std::string official_basic_type_from_preset_name(const std::string& preset_name);
- filament_type_for_color_decompose · function · L72-L72 — std::string filament_type_for_color_decompose(Preset* preset);
- find_existing_decompose_component · function · L74-L78 — int find_existing_decompose_component(
- prepare_decompose_mixed_result · function · L80-L88 — bool prepare_decompose_mixed_result(
- count_decompose_new_physical_filaments · function · L92-L97 — size_t count_decompose_new_physical_filaments(
- confirm_create_decompose_missing_components · function · L99-L100 — bool confirm_create_decompose_missing_components(wxWindow* parent,
