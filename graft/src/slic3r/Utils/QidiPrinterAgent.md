# src/slic3r/Utils/QidiPrinterAgent.hpp

- QidiPrinterAgent · class · L12-L48 — class QidiPrinterAgent final : public MoonrakerPrinterAgent
- QidiPrinterAgent · function · L15-L15 — explicit QidiPrinterAgent(std::string log_dir);
- get_agent_info_static · function · L18-L18 — static AgentInfo get_agent_info_static();
- get_agent_info · function · L19-L19 — AgentInfo        get_agent_info() override { return get_agent_info_static(); }
- fetch_filament_info · function · L22-L22 — bool fetch_filament_info(std::string dev_id) override;
- QidiFilamentDict · class · L25-L29 — struct QidiFilamentDict
- fetch_slot_info · function · L32-L38 — bool fetch_slot_info(const std::string&        base_url,
- fetch_filament_dict · function · L39-L39 — bool fetch_filament_dict(const std::string& base_url, const std::string& api_key, QidiFilamentDict& dict, std::string& error) const;
- normalize_filament_type · function · L40-L40 — std::string normalize_filament_type(const std::string& filament_type);
- infer_series_id · function · L41-L41 — std::string infer_series_id(const std::string& model_id, const std::string& dev_name);
- normalize_model_key · function · L42-L42 — std::string normalize_model_key(std::string value);
- parse_ini_section · function · L45-L45 — static void parse_ini_section(const std::string& content, const std::string& section_name, std::map<int, std::string>& result);
- parse_filament_sections · function · L46-L46 — static void parse_filament_sections(const std::string& content, std::map<int, std::string>& result);
- map_filament_type_to_setting_id · function · L47-L47 — static std::string map_filament_type_to_setting_id(const std::string& filament_type);
