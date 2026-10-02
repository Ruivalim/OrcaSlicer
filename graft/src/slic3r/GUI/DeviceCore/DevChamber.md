# src/slic3r/GUI/DeviceCore/DevChamber.h

- HasChamber · function · L15-L15 — bool HasChamber() const;
- SupportChamberTempDisplay · function · L16-L23 — bool SupportChamberTempDisplay() const;
- SupportChamberEdit · function · L17-L17 — bool SupportChamberEdit() const;
- GetChamberTempEditMin · function · L18-L18 — int  GetChamberTempEditMin() const;
- GetChamberTempEditMax · function · L19-L19 — int  GetChamberTempEditMax() const;
- GetChamberTempSwitchHeat · function · L20-L20 — int  GetChamberTempSwitchHeat() const;
- GetChamberTemp · function · L22-L22 — float GetChamberTemp() const { return m_temp; };
- GetChamberTempTarget · function · L23-L23 — float GetChamberTempTarget() const { return m_temp_target; };
- ParseChamber · function · L27-L27 — void ParseChamber(const json &print_json);
- ParseChamberV1_0 · function · L29-L29 — void ParseChamberV1_0(const json& print_json);
- ParseChamberV2_0 · function · L30-L30 — void ParseChamberV2_0(const json& print_json);
- CtrlSetChamberTemp · function · L33-L33 — int CtrlSetChamberTemp(int temp);
