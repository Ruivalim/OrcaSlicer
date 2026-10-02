# src/slic3r/GUI/DownloaderFileGet.hpp

- FileGet · class · L14-L30 — class FileGet : public std::enable_shared_from_this<FileGet>
- FileGet · function · L18-L18 — FileGet(int ID, std::string url, const std::string& filename, wxEvtHandler* evt_handler,const boost::filesystem::path& dest_folder);
- FileGet · function · L19-L19 — FileGet(FileGet&& other);
- get · function · L22-L22 — void get();
- cancel · function · L23-L23 — void cancel();
- pause · function · L24-L24 — void pause();
- resume · function · L25-L25 — void resume();
- escape_url · function · L26-L26 — static std::string	escape_url(const std::string& url);
- is_subdomain · function · L27-L27 — static bool			is_subdomain(const std::string& url, const std::string& domain);
