# src/libslic3r/Format/ResourcePathUtils.hpp

- ascii_lower_copy · function · L16-L23 — inline std::string ascii_lower_copy(const std::string& value)
- portable_path_copy · function · L25-L30 — inline boost::filesystem::path portable_path_copy(const boost::filesystem::path& value)
- hex_digit_value · function · L32-L38 — inline int hex_digit_value(char ch)
- percent_decode_copy · function · L43-L60 — inline std::string percent_decode_copy(const std::string& value)
- strip_file_uri_prefix_copy · function · L62-L78 — inline std::string strip_file_uri_prefix_copy(const std::string& value)
- file_uri_has_remote_authority · function · L80-L93 — inline bool file_uri_has_remote_authority(const std::string& value)
- looks_like_windows_absolute_path · function · L95-L102 — inline bool looks_like_windows_absolute_path(const boost::filesystem::path& path)
- filename_from_portable_path · function · L104-L108 — inline boost::filesystem::path filename_from_portable_path(const boost::filesystem::path& value)
- find_child_case_insensitive · function · L110-L136 — inline boost::filesystem::path find_child_case_insensitive(
- it · function · L122-L122 — for (boost::filesystem::directory_iterator it(directory, ec), end; !ec && it != end; it.increment(ec))
- resolve_existing_path_case_insensitive · function · L138-L181 — inline boost::filesystem::path resolve_existing_path_case_insensitive(
- resolve_existing_relative_path_case_insensitive · function · L183-L190 — inline boost::filesystem::path resolve_existing_relative_path_case_insensitive(
- resolve_external_resource_path · function · L203-L235 — inline boost::filesystem::path resolve_external_resource_path(
