# src/libslic3r/miniz_extension.hpp

- open_zip_reader · function · L9-L9 — bool open_zip_reader(mz_zip_archive *zip, const std::string &fname_utf8);
- open_zip_writer · function · L10-L10 — bool open_zip_writer(mz_zip_archive *zip, const std::string &fname_utf8);
- close_zip_reader · function · L11-L11 — bool close_zip_reader(mz_zip_archive *zip);
- close_zip_writer · function · L12-L12 — bool close_zip_writer(mz_zip_archive *zip);
- decode_archive_entry_path · function · L13-L13 — std::string decode_archive_entry_path(mz_zip_archive *zip, const mz_zip_archive_file_stat &stat);
- MZ_Archive · class · L15-L32 — class MZ_Archive
- MZ_Archive · function · L19-L19 — MZ_Archive();
- get_errorstr · function · L21-L21 — static std::string get_errorstr(mz_zip_error mz_err);
- get_errorstr · function · L23-L26 — std::string get_errorstr() const
- is_alive · function · L28-L31 — bool is_alive() const
