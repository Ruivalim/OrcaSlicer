# src/slic3r/GUI/PluginProgressDialog.hpp

- PluginProgressDialog · class · L25-L68 — class PluginProgressDialog : public ProgressDialog
- PluginProgressDialog · function · L32-L37 — PluginProgressDialog(wxWindow*       parent,
- create_dialog · function · L41-L46 — static PluginProgressDialog* create_dialog(wxWindow*       parent,
- pulse · function · L47-L47 — static bool pulse(PluginProgressDialog* dialog, const wxString& message = wxEmptyString);
- update · function · L48-L48 — static bool update(PluginProgressDialog* dialog, int value, const wxString& message = wxEmptyString);
- start_pulse · function · L49-L49 — static void start_pulse(PluginProgressDialog* dialog, int interval_ms, const wxString& message = wxEmptyString);
- stop_pulse · function · L50-L50 — static void stop_pulse(PluginProgressDialog* dialog);
- request_close · function · L51-L51 — static void request_close(PluginProgressDialog* dialog);
- pulse · function · L54-L54 — bool pulse(const wxString& message = wxEmptyString);
- update · function · L55-L55 — bool update(int value, const wxString& message = wxEmptyString);
- start_pulse · function · L56-L56 — void start_pulse(int interval_ms, const wxString& message = wxEmptyString);
- stop_pulse · function · L57-L57 — void stop_pulse();
- close · function · L58-L58 — void close();
- is_open · function · L59-L59 — bool is_open() const { return m_open; }
- on_timer · function · L62-L62 — void on_timer(wxTimerEvent& event);
