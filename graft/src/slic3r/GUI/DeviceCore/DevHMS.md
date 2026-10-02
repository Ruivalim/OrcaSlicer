# src/slic3r/GUI/DeviceCore/DevHMS.h

- ParseHMSItems · function · L20-L20 — void                           ParseHMSItems(const json& hms_json);
- GetHMSItems · function · L21-L21 — const std::vector<DevHMSItem>& GetHMSItems() const { return m_hms_list; };
- HMSMessageLevel · type · L30-L38 — enum HMSMessageLevel
- ModuleID · type · L40-L59 — enum ModuleID
- get_long_error_code · function · L64-L64 — std::string get_long_error_code() const;
- get_level · function · L65-L65 — HMSMessageLevel get_level() const { return m_msg_level; }
- set_read · function · L67-L67 — void set_read() { m_already_read = true; };
- has_read · function · L68-L68 — bool has_read() const { return m_already_read; };
- parse_hms_info · function · L72-L72 — bool parse_hms_info(unsigned attr, unsigned code);
