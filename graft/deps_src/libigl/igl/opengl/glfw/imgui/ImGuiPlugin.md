# deps_src/libigl/igl/opengl/glfw/imgui/ImGuiPlugin.h

- init · function · L45-L45 — IGL_INLINE virtual void init(igl::opengl::glfw::Viewer *_viewer) override;
- init_widgets · function · L46-L46 — IGL_INLINE void init_widgets();
- reload_font · function · L47-L47 — IGL_INLINE virtual void reload_font(int font_size = 13);
- shutdown · function · L48-L48 — IGL_INLINE virtual void shutdown() override;
- pre_draw · function · L49-L49 — IGL_INLINE virtual bool pre_draw() override;
- post_draw · function · L50-L50 — IGL_INLINE virtual bool post_draw() override;
- post_resize · function · L51-L51 — IGL_INLINE virtual void post_resize(int width, int height) override;
- mouse_down · function · L52-L52 — IGL_INLINE virtual bool mouse_down(int button, int modifier) override;
- mouse_up · function · L53-L53 — IGL_INLINE virtual bool mouse_up(int button, int modifier) override;
- mouse_move · function · L54-L54 — IGL_INLINE virtual bool mouse_move(int mouse_x, int mouse_y) override;
- mouse_scroll · function · L55-L55 — IGL_INLINE virtual bool mouse_scroll(float delta_y) override;
- key_pressed · function · L57-L57 — IGL_INLINE virtual bool key_pressed(unsigned int key, int modifiers) override;
- key_down · function · L58-L58 — IGL_INLINE virtual bool key_down(int key, int modifiers) override;
- key_up · function · L59-L59 — IGL_INLINE virtual bool key_up(int key, int modifiers) override;
- draw_text · function · L60-L64 — IGL_INLINE void draw_text(
- pixel_ratio · function · L65-L65 — IGL_INLINE float pixel_ratio();
- hidpi_scaling · function · L66-L66 — IGL_INLINE float hidpi_scaling();
