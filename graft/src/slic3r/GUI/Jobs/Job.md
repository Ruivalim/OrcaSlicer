# src/slic3r/GUI/Jobs/Job.hpp

- Job · class · L17-L64 — class Job
- JobPrepareState · type · L20-L23 — enum JobPrepareState
- Ctl · class · L27-L48 — class Ctl
- update_status · function · L32-L32 — virtual void update_status(int st, const std::string &msg = "") = 0;
- was_canceled · function · L35-L35 — virtual bool was_canceled() const = 0;
- clear_percent · function · L38-L38 — virtual void clear_percent()                                                                                             = 0;
- show_error_info · function · L39-L39 — virtual void show_error_info(const std::string &msg, int code, const std::string &description, const std::string &extra) = 0;
- call_on_main_thread · function · L47-L47 — virtual std::future<void> call_on_main_thread(std::function<void()> fn) = 0;
- process · function · L54-L54 — virtual void process(Ctl &ctl) = 0;
- finalize · function · L63-L63 — virtual void finalize(bool /*canceled*/, std::exception_ptr &) {}
