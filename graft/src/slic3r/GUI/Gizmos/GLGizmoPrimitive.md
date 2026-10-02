# src/slic3r/GUI/Gizmos/GLGizmoPrimitive.hpp

- GLGizmoPrimitive · class · L11-L38 — class GLGizmoPrimitive : public GLGizmoBase
- GLGizmoPrimitive · function · L14-L14 — GLGizmoPrimitive(GLCanvas3D& parent, const std::string& icon_filename, unsigned int sprite_id);
- on_mouse · function · L17-L17 — bool on_mouse(const wxMouseEvent& mouse_event) override;
- on_init · function · L20-L20 — bool on_init() override;
- on_get_name · function · L21-L21 — std::string on_get_name() const override;
- on_is_activable · function · L22-L22 — bool on_is_activable() const override;
- on_render · function · L23-L23 — void on_render() override;
- on_set_state · function · L24-L24 — void on_set_state() override;
- on_get_requirements · function · L25-L25 — CommonGizmosDataID on_get_requirements() const override;
- on_render_input_window · function · L26-L26 — void on_render_input_window(float x, float y, float bottom_limit) override;
- on_load · function · L28-L28 — void on_load(cereal::BinaryInputArchive& ar) override;
- on_save · function · L29-L29 — void on_save(cereal::BinaryOutputArchive& ar) const override;
- apply_primitive · function · L32-L32 — void apply_primitive();
- apply_preset · function · L33-L33 — void apply_preset(const char* name, double w, double h, double d);
