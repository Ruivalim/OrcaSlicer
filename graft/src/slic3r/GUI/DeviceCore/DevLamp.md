# src/slic3r/GUI/DeviceCore/DevLamp.h

- LIGHT_EFFECT · type · L15-L21 — enum LIGHT_EFFECT
- SetChamberLight · function · L24-L24 — void SetChamberLight(const std::string& status);
- SetChamberLight · function · L25-L25 — void SetChamberLight(LIGHT_EFFECT effect) { m_chamber_light = effect; }
- IsChamberLightOn · function · L26-L26 — bool IsChamberLightOn() const { return m_chamber_light == LIGHT_EFFECT_ON || m_chamber_light == LIGHT_EFFECT_FLASHING; }
- SetLampCloseRecheck · function · L28-L28 — void SetLampCloseRecheck(bool enable) { m_lamp_close_recheck = enable;};
- HasLampCloseRecheck · function · L29-L29 — bool HasLampCloseRecheck() const { return m_lamp_close_recheck; }
- CtrlSetChamberLight · function · L32-L32 — void CtrlSetChamberLight(LIGHT_EFFECT effect);
- command_set_chamber_light · function · L35-L35 — int command_set_chamber_light(LIGHT_EFFECT effect, int on_time = 500, int off_time = 500, int loops = 1, int interval = 1000);
- command_set_chamber_light2 · function · L36-L36 — int command_set_chamber_light2(LIGHT_EFFECT effect, int on_time = 500, int off_time = 500, int loops = 1, int interval = 1000);
