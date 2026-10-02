# src/slic3r/GUI/PublishDialog.hpp

- PublishStep · type · L30-L36 — enum PublishStep
- PublishDialog · class · L38-L65 — class PublishDialog : public DPIDialog
- PublishDialog · function · L41-L41 — PublishDialog(Plater* plater = nullptr);
- UpdateStatus · function · L43-L43 — bool UpdateStatus(wxString &msg, int percent = -1, bool yeild = true);
- Pulse · function · L44-L44 — void Pulse(wxString &msg, bool &skip);
- SetPublishStep · function · L45-L45 — void SetPublishStep(PublishStep step, bool yeild = false, int percent = -1);
- start_slicing · function · L46-L46 — void start_slicing();
- reset · function · L47-L47 — void reset();
- was_cancelled · function · L48-L48 — bool was_cancelled() { return m_was_cancelled; }
- cancel · function · L49-L49 — void cancel();
- create_publish_step_sizer · function · L62-L62 — wxBoxSizer* create_publish_step_sizer();
- on_close · function · L63-L63 — void on_close(wxCloseEvent &event);
- on_dpi_changed · function · L64-L64 — void on_dpi_changed(const wxRect &suggested_rect) override;
