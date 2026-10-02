# src/libslic3r/FileParserError.hpp

- file_parser_error · class · L13-L48 — class file_parser_error: public Slic3r::RuntimeError
- file_parser_error · function · L16-L18 — file_parser_error(const std::string &msg, const std::string &file, unsigned long line = 0) :
- file_parser_error · function · L19-L21 — file_parser_error(const std::string &msg, const boost::filesystem::path &file, unsigned long line = 0) :
- message · function · L27-L27 — std::string message() const { return m_message; }
- filename · function · L29-L29 — std::string filename() const { return m_filename; }
- line · function · L31-L31 — unsigned long line() const { return m_line; }
- format_what · function · L39-L47 — static std::string format_what(const std::string &msg, const std::string &file, unsigned long l)
