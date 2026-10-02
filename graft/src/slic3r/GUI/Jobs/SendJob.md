# src/slic3r/GUI/Jobs/SendJob.hpp

- Plater · class · L15-L15 — class Plater;
- OnUpdateStatusFn · type · L17-L17 — typedef std::function<void(int status, int code, std::string msg)> OnUpdateStatusFn;
- WasCancelledFn · type · L18-L18 — typedef std::function<bool()>                       WasCancelledFn;
- SendJob · class · L20-L71 — class SendJob : public Job
- prepare · function · L36-L36 — void prepare();
- SendJob · function · L37-L37 — SendJob(std::string dev_id = "");
- status_range · function · L56-L59 — int  status_range() const
- get_http_error_msg · function · L61-L61 — wxString get_http_error_msg(unsigned int status, std::string body);
- set_check_mode · function · L62-L62 — void set_check_mode() {m_is_check_mode = true;};
- check_and_continue · function · L63-L63 — void check_and_continue() {m_check_and_continue = true;};
- is_finished · function · L64-L64 — bool is_finished() { return m_job_finished;  }
- process · function · L65-L65 — void process(Ctl &ctl) override;
- on_success · function · L66-L66 — void on_success(std::function<void()> success);
- on_check_ip_address_fail · function · L67-L67 — void on_check_ip_address_fail(std::function<void(int)> func);
- on_check_ip_address_success · function · L68-L68 — void on_check_ip_address_success(std::function<void()> func);
- finalize · function · L69-L69 — void finalize(bool canceled, std::exception_ptr &) override;
- set_project_name · function · L70-L70 — void set_project_name(std::string name);
