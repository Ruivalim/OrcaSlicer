# src/slic3r/GUI/Calibration.hpp

- CalibrationDialog · class · L37-L67 — class CalibrationDialog : public DPIDialog
- create_check_option · function · L49-L49 — wxWindow* create_check_option(wxString title, wxWindow *parent, wxString tooltip, std::string param);
- CalibrationDialog · function · L52-L52 — CalibrationDialog(Plater *plater = nullptr);
- on_dpi_changed · function · L54-L54 — void on_dpi_changed(const wxRect &suggested_rect) override;
- update_cali · function · L62-L62 — void             update_cali(MachineObject *obj);
- is_stage_list_info_changed · function · L63-L63 — bool             is_stage_list_info_changed(MachineObject *obj);
- on_start_calibration · function · L64-L64 — void             on_start_calibration(wxMouseEvent &event);
- update_machine_obj · function · L65-L65 — void             update_machine_obj(MachineObject *obj);
- Show · function · L66-L66 — bool             Show(bool show) override;
