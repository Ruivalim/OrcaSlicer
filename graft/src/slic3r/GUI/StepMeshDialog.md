# src/slic3r/GUI/StepMeshDialog.hpp

- Button · class · L9-L9 — class Button;
- StepMeshDialog · class · L11-L52 — class StepMeshDialog : public Slic3r::GUI::DPIDialog
- StepMeshDialog · function · L14-L14 — StepMeshDialog(wxWindow* parent, Slic3r::Step& file, double linear_init, double angle_init);
- on_dpi_changed · function · L16-L16 — void on_dpi_changed(const wxRect& suggested_rect) override;
- get_linear_deflection · function · L17-L24 — inline double get_linear_deflection()
- get_angle_deflection · function · L25-L32 — inline double get_angle_deflection()
- get_split_compound_value · function · L33-L35 — inline bool get_split_compound_value()
- validate_number_range · function · L48-L48 — bool validate_number_range(const wxString& value, double min, double max);
- update_mesh_number_text · function · L49-L49 — void update_mesh_number_text();
- on_task_done · function · L50-L50 — void on_task_done(wxCommandEvent& event);
- stop_task · function · L51-L51 — void stop_task();
