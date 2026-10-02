# src/slic3r/GUI/DeviceCore/DevFan.h

- AirDuctType · type · L11-L11 — enum AirDuctType { AIR_FAN_TYPE, AIR_DOOR_TYPE };
- CommandCallBack · type · L12-L12 — typedef std::function<void(const json &)> CommandCallBack;
- AIR_FUN · type · L14-L24 — enum AIR_FUN : int
- AIR_DOOR · type · L26-L26 — enum AIR_DOOR { AIR_DOOR_FUNC_CHAMBER = 0, AIR_DOOR_FUNC_INNERLOOP, AIR_DOOR_FUNC_TOP };
- AIR_DUCT · type · L29-L36 — enum AIR_DUCT : int
- AirParts · class · L38-L40 — struct AirParts
- AirMode · class · L54-L56 — struct AirMode
- AirDuctData · class · L69-L71 — struct AirDuctData
- IsSupportCoolingFilter · function · L90-L90 — bool IsSupportCoolingFilter() const { return m_support_cooling_filter; }
- IsCoolingFilerOn · function · L91-L91 — bool IsCoolingFilerOn() const { return m_sub_mode == 1; }
- IsExaustFanExit · function · L92-L92 — bool IsExaustFanExit() const
- parts · function · L94-L95 — for (auto &p : parts)
- DevFan · function · L104-L104 — DevFan(MachineObject *obj) : m_owner(obj){};
