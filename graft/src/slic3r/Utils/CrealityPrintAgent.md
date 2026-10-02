# src/slic3r/Utils/CrealityPrintAgent.hpp

- PresetCollection · class · L11-L11 — class PresetCollection;
- CrealityPrintAgent · class · L25-L63 — class CrealityPrintAgent final : public MoonrakerPrinterAgent
- CFSSlot · class · L28-L36 — struct CFSSlot
- CrealityPrintAgent · function · L38-L38 — explicit CrealityPrintAgent(std::string log_dir);
- get_agent_info_static · function · L41-L41 — static AgentInfo get_agent_info_static();
- get_agent_info · function · L42-L42 — AgentInfo        get_agent_info() override { return get_agent_info_static(); }
- fetch_filament_info · function · L44-L44 — bool fetch_filament_info(std::string dev_id) override;
- parse_cfs_response · function · L48-L51 — static bool parse_cfs_response(const std::string&    response,
- normalize_filament_type · function · L55-L55 — static std::string normalize_filament_type(const std::string& filament_type);
- match_filament_preset · function · L59-L62 — static std::string match_filament_preset(const PresetCollection& filaments,
