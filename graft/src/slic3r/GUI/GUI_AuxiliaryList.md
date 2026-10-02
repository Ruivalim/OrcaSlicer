# src/slic3r/GUI/GUI_AuxiliaryList.hpp

- AuxiliaryList · class · L16-L49 — class AuxiliaryList : public wxDataViewCtrl
- AuxiliaryList · function · L19-L19 — AuxiliaryList(wxWindow* parent);
- get_top_sizer · function · L21-L21 — wxSizer* get_top_sizer() { return m_sizer; }
- init_auxiliary · function · L22-L22 — void init_auxiliary();
- reload · function · L23-L23 — void reload(wxString aux_path);
- do_import_file · function · L26-L26 — void do_import_file(AuxiliaryModelNode* folder);
- on_create_folder · function · L27-L27 — void on_create_folder(wxCommandEvent& evt);
- on_import_file · function · L28-L28 — void on_import_file(wxCommandEvent& evt);
- on_delete · function · L29-L29 — void on_delete(wxCommandEvent& evt);
- on_context_menu · function · L30-L30 — void on_context_menu(wxDataViewEvent& evt);
- on_begin_drag · function · L31-L31 — void on_begin_drag(wxDataViewEvent& evt);
- on_drop_possible · function · L32-L32 — void on_drop_possible(wxDataViewEvent& evt);
- on_drop · function · L33-L33 — void on_drop(wxDataViewEvent& evt);
- on_editing_started · function · L34-L34 — void on_editing_started(wxDataViewEvent& evt);
- on_editing_done · function · L35-L35 — void on_editing_done(wxDataViewEvent& evt);
- on_left_dclick · function · L36-L36 — void on_left_dclick(wxMouseEvent& evt);
- create_new_folder · function · L38-L38 — void create_new_folder();
- handle_key_event · function · L39-L39 — void handle_key_event(wxKeyEvent& evt);
