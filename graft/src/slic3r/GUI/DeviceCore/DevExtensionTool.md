# src/slic3r/GUI/DeviceCore/DevExtensionTool.h

- IsToolTypeFanF000 · function · L25-L25 — bool IsToolTypeFanF000() const { return m_tool_type == TOOL_TYPE_FAN_F000; }
- IsMounted · function · L28-L28 — bool IsMounted() const { return m_mount_3dp == MOUNT_MOUNTED; }
- MountState · type · L36-L42 — enum MountState
- CalibState · type · L44-L49 — enum CalibState
- ToolType · type · L51-L57 — enum ToolType
- ParseV2_0 · function · L64-L64 — static void ParseV2_0(const nlohmann::json& extension_tool_json, std::weak_ptr<DevExtensionTool> extension_tool);
