# src/slic3r/GUI/Gizmos/GLGizmoFaceDetector.hpp

- GLGizmoFaceDetector · class · L11-L33 — class GLGizmoFaceDetector : public GLGizmoBase
- GLGizmoFaceDetector · function · L14-L15 — GLGizmoFaceDetector(GLCanvas3D& parent, const std::string& icon_filename, unsigned int sprite_id)
- on_render · function · L18-L18 — void on_render() override;
- on_render_for_picking · function · L19-L19 — void on_render_for_picking() override {}
- on_render_input_window · function · L20-L20 — void on_render_input_window(float x, float y, float bottom_limit) override;
- on_get_name · function · L21-L21 — std::string on_get_name() const override;
- on_set_state · function · L22-L22 — void on_set_state() override;
- on_is_activable · function · L23-L23 — bool on_is_activable() const override;
- on_get_requirements · function · L24-L24 — CommonGizmosDataID on_get_requirements() const override;
- on_init · function · L27-L27 — bool on_init() override;
- perform_recognition · function · L28-L28 — void perform_recognition(const Selection& selection);
- display_exterior_face · function · L29-L29 — void display_exterior_face();
