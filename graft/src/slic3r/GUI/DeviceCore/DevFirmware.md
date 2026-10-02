# src/slic3r/GUI/DeviceCore/DevFirmware.h

- PrinterFirmwareType · type · L15-L20 — enum PrinterFirmwareType
- isValid · function · L45-L45 — bool isValid() const { return !sn.empty(); }
- isAirPump · function · L48-L48 — bool isAirPump() const { return product_name.Contains("Air Pump"); }
- isLaszer · function · L49-L49 — bool isLaszer() const { return product_name.Contains("Laser"); }
- isCuttingModule · function · L50-L50 — bool isCuttingModule() const { return product_name.Contains("Cutting Module"); }
- isRotary · function · L51-L51 — bool isRotary() const { return product_name.Contains("Rotary"); }// Rotary Attachment
- isExtinguishSystem · function · L52-L52 — bool isExtinguishSystem() const { return product_name.Contains("Extinguishing System"); }// Auto Fire Extinguishing System
- isWTM · function · L53-L53 — bool isWTM() const { return name.find("wtm") != string::npos; } // nozzle
- isExhaustFan · function · L54-L54 — bool isExhaustFan() const { return product_name.Contains("Exhaust Fan"); }
- isHmshub · function · L55-L55 — bool isHmshub() const { return product_name.find("Filament Buffer") != string::npos; }
- isFilaTrackSwitch · function · L56-L56 — bool isFilaTrackSwitch() const { return product_name.find("Filament Track") != string::npos; }
