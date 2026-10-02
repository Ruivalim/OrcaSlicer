# src/slic3r/GUI/Widgets/FilamentLoad.hpp

- FilamentLoad · class · L22-L60 — class FilamentLoad : public wxSimplebook
- FilamentLoad · function · L25-L25 — FilamentLoad(wxWindow* parent, wxWindowID id = wxID_ANY, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxDefaultSize);
- SetAmsModel · function · L46-L46 — void SetAmsModel(AMSModel mode, AMSModel ext_mode) { m_ams_model = mode; m_ext_model = ext_mode; };
- SetFilamentStep · function · L48-L48 — void SetFilamentStep(FilamentStep item_idx, FilamentStepType f_type);
- ShowFilamentTip · function · L49-L49 — void ShowFilamentTip(bool hasams = true);
- SetupSteps · function · L51-L51 — void SetupSteps(MachineObject* obj_, bool is_extrusion_exist);
- show_nofilament_mode · function · L53-L53 — void show_nofilament_mode(bool show);
- updateID · function · L54-L54 — void updateID(int ams_id, int slot_id) { m_ams_id = ams_id; m_slot_id = slot_id; };
- SetExt · function · L55-L55 — void SetExt(bool ext) { is_extrusion = ext; };
- set_min_size · function · L57-L57 — void set_min_size(const wxSize& minSize);
- set_max_size · function · L58-L58 — void set_max_size(const wxSize& maxSize);
- set_background_color · function · L59-L59 — void set_background_color(const wxColour& colour);
