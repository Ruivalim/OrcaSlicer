# src/slic3r/GUI/DeviceCore/DevAxis.h

- DevAxis · function · L13-L13 — virtual ~DevAxis() = default;
- IsAxisAtHomeX · function · L16-L16 — bool IsAxisAtHomeX() const { return m_home_flag == 0 ? true : (m_home_flag & 1) == 1; }
- IsAxisAtHomeY · function · L17-L17 — bool IsAxisAtHomeY() const { return m_home_flag == 0 ? true : ((m_home_flag >> 1) & 1) == 1; }
- IsAxisAtHomeZ · function · L18-L18 — bool IsAxisAtHomeZ() const { return m_home_flag == 0 ? true : ((m_home_flag >> 2) & 1) == 1; }
- IsArchCoreXY · function · L20-L20 — bool IsArchCoreXY() const;
- ParseAxis · function · L23-L23 — void ParseAxis(const json &print_json);
- Ctrl_GoHome · function · L25-L25 — int Ctrl_GoHome();
- Ctrl_Axis · function · L26-L26 — int Ctrl_Axis(std::string axis, double unit = 1.0f, double input_val = 1.0f, int speed = 3000); // xyz e
