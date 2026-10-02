# src/slic3r/GUI/Gizmos/GLGizmoFuzzySkin.hpp

- GLGizmoFuzzySkin · class · L10-L55 — class GLGizmoFuzzySkin : public GLGizmoPainterBase
- GLGizmoFuzzySkin · function · L13-L13 — GLGizmoFuzzySkin(GLCanvas3D& parent, const std::string& icon_filename, unsigned int sprite_id);
- render_painter_gizmo · function · L15-L15 — void render_painter_gizmo() override;
- on_render_input_window · function · L18-L18 — void        on_render_input_window(float x, float y, float bottom_limit) override;
- on_get_name · function · L19-L19 — std::string on_get_name() const override;
- render_tooltip_button · function · L21-L21 — void render_tooltip_button(float x, float y);
- handle_snapshot_action_name · function · L23-L23 — wxString handle_snapshot_action_name(bool shift_down, Button button_down) const override;
- get_gizmo_entering_text · function · L25-L25 — std::string get_gizmo_entering_text() const override { return _u8L("Entering Paint-on fuzzy skin"); }
- get_gizmo_leaving_text · function · L26-L26 — std::string get_gizmo_leaving_text() const override { return _u8L("Leaving Paint-on fuzzy skin"); }
- get_action_snapshot_name · function · L27-L27 — std::string get_action_snapshot_name() const override { return _u8L("Paint-on fuzzy skin editing"); }
- get_left_button_state_type · function · L29-L29 — EnforcerBlockerType get_left_button_state_type() const override { return EnforcerBlockerType::FUZZY_SKIN; }
- get_right_button_state_type · function · L30-L30 — EnforcerBlockerType get_right_button_state_type() const override { return EnforcerBlockerType::NONE; }
- on_init · function · L36-L36 — bool on_init() override;
- update_model_object · function · L38-L38 — void update_model_object() override;
- update_from_model_object · function · L39-L39 — void update_from_model_object(bool first_update) override;
- on_opening · function · L41-L41 — void             on_opening() override {}
- on_shutdown · function · L42-L42 — void             on_shutdown() override;
- get_painter_type · function · L43-L43 — PainterGizmoType get_painter_type() const override;
