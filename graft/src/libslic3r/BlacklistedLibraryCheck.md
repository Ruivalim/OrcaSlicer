# src/libslic3r/BlacklistedLibraryCheck.hpp

- BlacklistedLibraryCheck · class · L13-L40 — class BlacklistedLibraryCheck
- get_instance · function · L16-L16 — static BlacklistedLibraryCheck& get_instance()
- BlacklistedLibraryCheck · function · L23-L23 — BlacklistedLibraryCheck() = default;
- BlacklistedLibraryCheck · function · L27-L27 — BlacklistedLibraryCheck(BlacklistedLibraryCheck const&) = delete;
- get_blacklisted · function · L30-L30 — bool get_blacklisted(std::vector<std::wstring>& names);
- get_blacklisted_string · function · L31-L31 — std::wstring get_blacklisted_string();
- perform_check · function · L33-L33 — bool perform_check();
- is_blacklisted · function · L36-L36 — static bool is_blacklisted(const std::string &dllpath);
- is_blacklisted · function · L37-L37 — static bool is_blacklisted(const std::wstring &dllpath);
