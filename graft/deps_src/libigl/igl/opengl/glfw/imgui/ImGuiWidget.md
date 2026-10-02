# deps_src/libigl/igl/opengl/glfw/imgui/ImGuiWidget.h

- ImGuiWidget · function · L33-L33 — IGL_INLINE ImGuiWidget(){ name = "dummy"; }
- ImGuiWidget · function · L34-L34 — virtual ~ImGuiWidget(){}
- init · function · L35-L36 — IGL_INLINE virtual void init(Viewer *_viewer, ImGuiPlugin *_plugin)
- shutdown · function · L37-L37 — IGL_INLINE virtual void shutdown() {}
- draw · function · L38-L38 — IGL_INLINE virtual void draw() {}
- mouse_down · function · L39-L40 — IGL_INLINE virtual bool mouse_down(int /*button*/, int /*modifier*/)
- mouse_up · function · L41-L42 — IGL_INLINE virtual bool mouse_up(int /*button*/, int /*modifier*/)
- mouse_move · function · L43-L44 — IGL_INLINE virtual bool mouse_move(int /*mouse_x*/, int /*mouse_y*/)
- key_pressed · function · L45-L46 — IGL_INLINE virtual bool key_pressed(unsigned int /*key*/, int /*modifiers*/)
- key_down · function · L47-L48 — IGL_INLINE virtual bool key_down(int /*key*/, int /*modifiers*/)
- key_up · function · L49-L50 — IGL_INLINE virtual bool key_up(int /*key*/, int /*modifiers*/)
