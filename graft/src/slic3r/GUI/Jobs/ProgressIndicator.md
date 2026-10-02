# src/slic3r/GUI/Jobs/ProgressIndicator.hpp

- ProgressIndicator · class · L13-L28 — class ProgressIndicator
- clear_percent · function · L21-L21 — virtual void clear_percent() = 0;
- show_error_info · function · L22-L22 — virtual void show_error_info(wxString msg, int code, wxString description, wxString extra) = 0;
- set_range · function · L23-L23 — virtual void set_range(int range) = 0;
- set_cancel_callback · function · L24-L24 — virtual void set_cancel_callback(CancelFn = CancelFn()) = 0;
- set_progress · function · L25-L25 — virtual void set_progress(int pr) = 0;
- set_status_text · function · L26-L26 — virtual void set_status_text(const char *) = 0; // utf8 char array
- get_range · function · L27-L27 — virtual int  get_range() const = 0;
