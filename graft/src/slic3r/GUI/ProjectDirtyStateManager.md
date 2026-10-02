# src/slic3r/GUI/ProjectDirtyStateManager.hpp

- ProjectDirtyStateManager · class · L9-L60 — class ProjectDirtyStateManager
- update_from_undo_redo_stack · function · L12-L12 — void update_from_undo_redo_stack(bool dirty);
- update_from_presets · function · L13-L13 — void update_from_presets();
- reset_after_save · function · L14-L14 — void reset_after_save();
- reset_initial_presets · function · L15-L15 — void reset_initial_presets();
- set_plater_dirty · function · L17-L17 — void set_plater_dirty(bool is_dirty);
- is_dirty · function · L18-L18 — bool is_dirty() const { return m_plater_dirty || m_project_config_dirty || m_presets_dirty; }
- is_presets_dirty · function · L19-L19 — bool is_presets_dirty() const { return m_presets_dirty; }
- NotificationSuppressor · class · L24-L33 — class NotificationSuppressor
- NotificationSuppressor · function · L27-L27 — explicit NotificationSuppressor(ProjectDirtyStateManager &owner) : m_owner(owner) { m_owner.begin_suppress_notifications(); }
- NotificationSuppressor · function · L29-L29 — NotificationSuppressor(const NotificationSuppressor &) = delete;
- render_debug_window · function · L36-L36 — void render_debug_window() const;
- notify_dirty_change · function · L40-L40 — void notify_dirty_change(bool was_dirty, const char *source);
- begin_suppress_notifications · function · L41-L41 — void begin_suppress_notifications();
- end_suppress_notifications · function · L42-L42 — void end_suppress_notifications();
