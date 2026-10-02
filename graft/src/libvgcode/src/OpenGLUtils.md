# src/libvgcode/src/OpenGLUtils.hpp

- glAssertRecentCallImpl · function · L23-L23 — extern void glAssertRecentCallImpl(const char* file_name, unsigned int line, const char* function_name);
- glAssertRecentCall · function · L24-L24 — inline void glAssertRecentCall() { glAssertRecentCallImpl(__FILE__, __LINE__, __FUNCTION__); }
- glAssertRecentCall · function · L28-L28 — inline void glAssertRecentCall() { }
- OpenGLWrapper · class · L33-L48 — class OpenGLWrapper
- load_opengl · function · L36-L36 — static bool load_opengl(const std::string& context_version);
- unload_opengl · function · L37-L37 — static void unload_opengl();
- is_valid_context · function · L38-L38 — static bool is_valid_context() { return s_valid_context; }
- max_texture_size · function · L40-L40 — static size_t max_texture_size() { return static_cast<size_t>(s_max_texture_size); }
