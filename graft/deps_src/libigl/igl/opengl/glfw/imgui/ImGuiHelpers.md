# deps_src/libigl/igl/opengl/glfw/imgui/ImGuiHelpers.h

- Combo · function · L36-L41 — inline bool Combo(const char* label, int* idx, std::vector<std::string>& values)
- Combo · function · L43-L50 — inline bool Combo(const char* label, int* idx, std::function<const char *(int)> getter, int items_count)
- ListBox · function · L54-L59 — inline bool ListBox(const char* label, int* idx, std::vector<std::string>& values)
- InputText · function · L61-L61 — inline bool InputText(const char* label, std::string &str, ImGuiInputTextFlags flags = 0, ImGuiInputTextCallback callback = NULL, void* user_data = NULL)
- SliderScalar · function · L95-L95 — inline bool SliderScalar(const char *label, T* value, T min = 0, T max = 0, const char* format = "")
- Checkbox · function · L105-L111 — inline bool Checkbox(const char* label, Getter get, Setter set)
