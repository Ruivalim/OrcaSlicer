# src/slic3r/GUI/SafetyOptionsDialog.hpp

- SwitchBoard · class · L21-L21 — class SwitchBoard;
- SafetyOptionsDialog · class · L25-L62 — class SafetyOptionsDialog : public DPIDialog
- create_settings_group · function · L44-L44 — wxBoxSizer* create_settings_group(wxWindow* parent);
- SafetyOptionsDialog · function · L48-L48 — SafetyOptionsDialog(wxWindow* parent);
- on_dpi_changed · function · L50-L50 — void on_dpi_changed(const wxRect &suggested_rect) override;
- update_options · function · L54-L54 — void             update_options(MachineObject *obj_);
- update_machine_obj · function · L55-L55 — void             update_machine_obj(MachineObject *obj_);
- Show · function · L56-L56 — bool             Show(bool show) override;
- updateOpenDoorCheck · function · L59-L59 — void updateOpenDoorCheck(MachineObject *obj);
- updateIdelHeatingProtect · function · L60-L60 — void updateIdelHeatingProtect(MachineObject *obj);
- show_idel_heating_toast · function · L61-L61 — void show_idel_heating_toast(const wxString &text);
