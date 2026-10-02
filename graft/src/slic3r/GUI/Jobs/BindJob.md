# src/slic3r/GUI/Jobs/BindJob.hpp

- BindJob · class · L13-L42 — class BindJob : public Job
- BindJob · function · L26-L26 — BindJob(std::string dev_id, std::string dev_ip, std::string dev_model, std::string sec_link, std::string ssdp_version);
- status_range · function · L28-L31 — int  status_range() const
- is_finished · function · L33-L33 — bool is_finished() { return m_job_finished;  }
- on_success · function · L35-L35 — void on_success(std::function<void()> success);
- update_status · function · L36-L36 — void update_status(Ctl &ctl, int st, const std::string &msg);
- process · function · L37-L37 — void process(Ctl &ctl) override;
- finalize · function · L38-L38 — void finalize(bool canceled, std::exception_ptr &eptr) override;
- set_event_handle · function · L39-L39 — void set_event_handle(wxWindow* hanle);
- post_fail_event · function · L40-L40 — void post_fail_event(int code, std::string info);
- set_improved · function · L41-L41 — void set_improved(bool improved){m_improved = improved;};
