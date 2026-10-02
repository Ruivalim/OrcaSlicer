# src/slic3r/GUI/Jobs/NotificationProgressIndicator.hpp

- NotificationManager · class · L8-L8 — class NotificationManager;
- NotificationProgressIndicator · class · L10-L25 — class NotificationProgressIndicator: public ProgressIndicator
- NotificationProgressIndicator · function · L16-L16 — explicit NotificationProgressIndicator(NotificationManager *nm);
- clear_percent · function · L18-L18 — void clear_percent() override;
- show_error_info · function · L19-L19 — void show_error_info(wxString msg, int code, wxString description, wxString extra) override;
- set_range · function · L20-L20 — void set_range(int range) override;
- set_cancel_callback · function · L21-L21 — void set_cancel_callback(CancelFn = CancelFn()) override;
- set_progress · function · L22-L22 — void set_progress(int pr) override;
- set_status_text · function · L23-L23 — void set_status_text(const char *) override; // utf8 char array
- get_range · function · L24-L24 — int  get_range() const override;
