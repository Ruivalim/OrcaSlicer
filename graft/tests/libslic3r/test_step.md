# tests/libslic3r/test_step.cpp

- write_step_line · function · L11-L15 — static void write_step_line(const std::string &path, const std::string &line)
- file · function · L13-L13 — boost::nowide::ofstream file(path, std::ios::binary);
- preprocess_result · function · L18-L30 — static std::string preprocess_result(const std::string &line)
- step · function · L42-L42 — Step  step(path); // no isUtf8Fn, matching how Model::read_from_step builds it
