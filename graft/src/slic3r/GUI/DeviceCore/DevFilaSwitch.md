# src/slic3r/GUI/DeviceCore/DevFilaSwitch.h

- class · type · L15-L15 — enum class CaliStatus : int
- class · type · L21-L80 — enum class CaliStep : int
- SwitchPos · type · L33-L37 — enum SwitchPos : int
- DevFilaSwitch · function · L41-L41 — virtual ~DevFilaSwitch() = default;
- IsInstalled · function · L44-L44 — bool IsInstalled() const { return m_is_installed; };
- IsReady · function · L45-L45 — bool IsReady() const;
- GetCaliStatus · function · L60-L60 — CaliStatus GetCaliStatus() const { return m_cali_status; };
- Reset · function · L62-L62 — void Reset();
- ParseFilaSwitchInfo · function · L63-L63 — void ParseFilaSwitchInfo(const nlohmann::json& print_jj);
