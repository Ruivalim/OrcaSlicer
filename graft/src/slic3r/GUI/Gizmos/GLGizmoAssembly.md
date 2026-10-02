# src/slic3r/GUI/Gizmos/GLGizmoAssembly.hpp

- GLGizmoAssembly · class · L9-L38 — class GLGizmoAssembly : public GLGizmoMeasure
- GLGizmoAssembly · function · L13-L13 — GLGizmoAssembly(GLCanvas3D& parent, const std::string& icon_filename, unsigned int sprite_id);
- wants_enter_leave_snapshots · function · L23-L23 — bool wants_enter_leave_snapshots() const override { return true; }
- get_gizmo_entering_text · function · L24-L24 — std::string get_gizmo_entering_text() const override { return _u8L("Entering Assembly gizmo"); }
- get_gizmo_leaving_text · function · L25-L25 — std::string get_gizmo_leaving_text() const override { return _u8L("Leaving Assembly gizmo"); }
- on_init · function · L27-L27 — bool on_init() override;
- on_get_name · function · L28-L28 — std::string on_get_name() const override;
- on_is_activable · function · L29-L29 — bool on_is_activable() const override;
- on_render_input_window · function · L32-L32 — virtual void on_render_input_window(float x, float y, float bottom_limit) override;
- render_input_window_warning · function · L34-L34 — void render_input_window_warning(bool same_model_object) override;
- render_assembly_mode_combo · function · L35-L35 — bool render_assembly_mode_combo(double label_width, float item_width);
- switch_to_mode · function · L37-L37 — void switch_to_mode(AssemblyMode new_mode);
