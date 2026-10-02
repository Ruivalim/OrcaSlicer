# src/slic3r/Utils/Serial.hpp

- SerialPortInfo · class · L13-L24 — struct SerialPortInfo
- SerialPortInfo · function · L20-L20 — SerialPortInfo() {}
- SerialPortInfo · function · L21-L21 — SerialPortInfo(std::string port) : port(port), friendly_name(std::move(port)) {}
- id_match · function · L23-L23 — bool id_match(unsigned id_vendor, unsigned id_product) const { return id_vendor == this->id_vendor && id_product == this->id_product; }
- scan_serial_ports · function · L35-L35 — extern std::vector<std::string> 	scan_serial_ports();
- scan_serial_ports_extended · function · L36-L36 — extern std::vector<SerialPortInfo> 	scan_serial_ports_extended();
- Serial · class · L39-L91 — class Serial : public boost::asio::serial_port
- Serial · function · L42-L42 — Serial(boost::asio::io_service &io_service);
- Serial · function · L43-L43 — Serial(boost::asio::io_service &io_service, const std::string &name, unsigned baud_rate);
- Serial · function · L44-L44 — Serial(const Serial &) = delete;
- set_baud_rate · function · L48-L48 — void set_baud_rate(unsigned baud_rate);
