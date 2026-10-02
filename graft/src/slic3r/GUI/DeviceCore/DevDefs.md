# src/slic3r/GUI/DeviceCore/DevDefs.h

- PrinterArch · type · L24-L28 — enum PrinterArch
- PrinterSeries · type · L30-L35 — enum PrinterSeries
- AmsStatusMain · type · L41-L52 — enum AmsStatusMain
- DevAmsType · type · L54-L62 — enum DevAmsType : int
- DevFilamentStep · type · L64-L83 — enum DevFilamentStep
- NozzleFlowType · type · L112-L119 — enum NozzleFlowType : int
- NozzleDiameterType · type · L121-L128 — enum NozzleDiameterType : int
- DevPrintingSpeedLevel · type · L131-L139 — enum DevPrintingSpeedLevel
- class · type · L142-L175 — enum class DevFirmwareUpgradeState : int
- IsVirtualSlot · function · L162-L162 — static bool IsVirtualSlot(int ams_id) { return (ams_id == VIRTUAL_TRAY_MAIN_ID || ams_id == VIRTUAL_TRAY_DEPUTY_ID);}
- IsVirtualSlot · function · L163-L163 — static bool IsVirtualSlot(const std::string& ams_id) { return (ams_id == VIRTUAL_AMS_MAIN_ID_STR || ams_id == VIRTUAL_AMS_DEPUTY_ID_STR); }
- PrintFromType · type · L168-L172 — enum PrintFromType
- NozzleDef · class · L177-L185 — struct NozzleDef
- operator · function · L190-L190 — std::size_t operator()(const NozzleDef& v) const noexcept
