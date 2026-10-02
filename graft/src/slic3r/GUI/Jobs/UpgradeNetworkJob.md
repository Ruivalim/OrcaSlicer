# src/slic3r/GUI/Jobs/UpgradeNetworkJob.hpp

- PluginInstallStatus · type · L15-L21 — enum PluginInstallStatus
- InstallProgressFn · type · L23-L23 — typedef std::function<void(int status, int percent, bool& cancel)> InstallProgressFn;
- UpgradeNetworkJob · class · L25-L52 — class UpgradeNetworkJob : public Job
- UpgradeNetworkJob · function · L38-L38 — UpgradeNetworkJob();
- status_range · function · L40-L43 — int  status_range() const
- is_finished · function · L45-L45 — bool is_finished() { return m_job_finished;  }
- on_success · function · L47-L47 — void on_success(std::function<void()> success);
- update_status · function · L48-L48 — void update_status(Ctl &ctl, int st, const std::string &msg);
- process · function · L49-L49 — void process(Ctl &ctl) override;
- finalize · function · L50-L50 — void finalize(bool canceled, std::exception_ptr &e) override;
- set_event_handle · function · L51-L51 — void set_event_handle(wxWindow* hanle);
