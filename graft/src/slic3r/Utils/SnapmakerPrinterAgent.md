# src/slic3r/Utils/SnapmakerPrinterAgent.hpp

- SnapmakerPrinterAgent · class · L9-L23 — class SnapmakerPrinterAgent final : public MoonrakerPrinterAgent
- SnapmakerPrinterAgent · function · L12-L12 — explicit SnapmakerPrinterAgent(std::string log_dir);
- get_agent_info_static · function · L15-L15 — static AgentInfo get_agent_info_static();
- get_agent_info · function · L16-L16 — AgentInfo        get_agent_info() override { return get_agent_info_static(); }
- fetch_filament_info · function · L18-L18 — bool fetch_filament_info(std::string dev_id) override;
- combine_filament_type · function · L22-L22 — static std::string combine_filament_type(const std::string& type, const std::string& sub_type);
