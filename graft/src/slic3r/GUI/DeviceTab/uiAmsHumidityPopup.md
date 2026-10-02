# src/slic3r/GUI/DeviceTab/uiAmsHumidityPopup.h

- uiAmsHumidityInfo · class · L20-L28 — struct uiAmsHumidityInfo
- UpdateInfo · function · L41-L41 — void UpdateInfo(uiAmsHumidityInfo *info) { m_ams_id = info->ams_id; UpdateInfo(info->humidity_display_idx, info->humidity_percent, info->left_dry_time, info->current_temperature); };
- get_owner_ams_id · function · L43-L43 — std::string get_owner_ams_id() const { return m_ams_id; }
- msw_rescale · function · L45-L45 — void msw_rescale();
- UpdateInfo · function · L48-L48 — void UpdateInfo(int humidiy_level, int humidity_percent, int left_dry_time, float current_temperature);
- UpdateContents · function · L49-L49 — void UpdateContents();
- Create · function · L51-L51 — void Create();
