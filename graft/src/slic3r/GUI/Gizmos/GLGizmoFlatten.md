# src/slic3r/GUI/Gizmos/GLGizmoFlatten.hpp

- ModelVolumeType · type · L10-L10 — enum class ModelVolumeType : int;
- GLGizmoFlatten · class · L16-L66 — class GLGizmoFlatten : public GLGizmoBase
- PlaneData · class · L22-L28 — struct PlaneData
- update_planes · function · L41-L41 — void update_planes();
- is_plane_update_necessary · function · L42-L42 — bool is_plane_update_necessary() const;
- GLGizmoFlatten · function · L45-L45 — GLGizmoFlatten(GLCanvas3D& parent, const std::string& icon_filename, unsigned int sprite_id);
- set_flattening_data · function · L47-L47 — void set_flattening_data(const ModelObject* model_object, int instance_id);
- on_mouse · function · L54-L54 — bool on_mouse(const wxMouseEvent &mouse_event) override;
- data_changed · function · L56-L56 — void data_changed(bool is_serializing) override;
- on_init · function · L58-L58 — bool on_init() override;
- on_get_name · function · L59-L59 — std::string on_get_name() const override;
- on_is_activable · function · L60-L60 — bool on_is_activable() const override;
- on_render · function · L61-L61 — void on_render() override;
- on_register_raycasters_for_picking · function · L62-L62 — void on_register_raycasters_for_picking() override;
- on_unregister_raycasters_for_picking · function · L63-L63 — void on_unregister_raycasters_for_picking() override;
- on_set_state · function · L64-L64 — void on_set_state() override;
- on_get_requirements · function · L65-L65 — CommonGizmosDataID on_get_requirements() const override;
