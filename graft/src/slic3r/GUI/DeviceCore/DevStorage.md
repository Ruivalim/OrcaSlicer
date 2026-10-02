# src/slic3r/GUI/DeviceCore/DevStorage.h

- SdcardState · type · L17-L23 — enum SdcardState :  int
- get_sdcard_state · function · L26-L26 — SdcardState get_sdcard_state() const { return  m_sdcard_state; };
- set_sdcard_state · function · L27-L27 — SdcardState set_sdcard_state(int state);
- ParseV1_0 · function · L29-L29 — static void ParseV1_0(const json &print_json, DevStorage *system);
- is_timelapse_storage_low · function · L31-L31 — bool is_timelapse_storage_low(const std::string& storage) const;
