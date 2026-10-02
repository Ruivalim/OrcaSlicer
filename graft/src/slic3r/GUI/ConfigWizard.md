# src/slic3r/GUI/ConfigWizard.hpp

- PresetBundle · class · L12-L12 — class PresetBundle;
- PresetUpdater · class · L13-L13 — class PresetUpdater;
- ConfigWizard · class · L18-L58 — class ConfigWizard: public DPIDialog
- RunReason · type · L22-L27 — enum RunReason
- StartPage · type · L30-L36 — enum StartPage
- ConfigWizard · function · L38-L38 — ConfigWizard(wxWindow *parent);
- ConfigWizard · function · L39-L39 — ConfigWizard(ConfigWizard &&) = delete;
- ConfigWizard · function · L40-L40 — ConfigWizard(const ConfigWizard &) = delete;
- run · function · L46-L46 — bool run(RunReason reason, StartPage start_page = SP_WELCOME);
- name · function · L48-L48 — static const wxString& name(const bool from_menu = false);
- on_dpi_changed · function · L50-L50 — void on_dpi_changed(const wxRect &suggested_rect) override ;
- on_sys_color_changed · function · L51-L51 — void on_sys_color_changed() override;
