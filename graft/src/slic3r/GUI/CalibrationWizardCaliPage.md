# src/slic3r/GUI/CalibrationWizardCaliPage.hpp

- CalibrationCaliPage · class · L9-L49 — class CalibrationCaliPage : public CalibrationWizardPage
- CalibrationCaliPage · function · L12-L18 — CalibrationCaliPage(wxWindow* parent,
- create_page · function · L21-L21 — void create_page(wxWindow* parent);
- on_subtask_pause_resume · function · L22-L22 — void on_subtask_pause_resume(wxCommandEvent& event);
- on_subtask_abort · function · L23-L23 — void on_subtask_abort(wxCommandEvent& event);
- set_cali_img · function · L24-L24 — void set_cali_img();
- update · function · L25-L25 — void update(MachineObject* obj) override;
- update_subtask · function · L26-L26 — void update_subtask(MachineObject* obj);
- update_basic_print_data · function · L27-L27 — void update_basic_print_data(bool def, float weight = 0.0, int prediction = 0);
- reset_printing_values · function · L28-L28 — void reset_printing_values();
- clear_last_job_status · function · L29-L29 — void clear_last_job_status();
- set_pa_cali_image · function · L30-L30 — void set_pa_cali_image(int stage);
- on_device_connected · function · L32-L32 — void on_device_connected(MachineObject* obj) override;
- set_cali_method · function · L34-L34 — void set_cali_method(CalibrationMethod method) override;
- Show · function · L35-L35 — virtual bool Show(bool show = true) override;
- msw_rescale · function · L36-L36 — void msw_rescale() override;
- get_selected_calibration_nozzle_dia · function · L39-L39 — float get_selected_calibration_nozzle_dia(MachineObject* obj);
