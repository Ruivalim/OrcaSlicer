# tests/libslic3r/test_3mf.cpp

- is_eigen_matrix · class · L30-L31 — template <typename T>
- convert · function · L35-L42 — static std::string convert(const T& eigen_obj)
- convert · function · L49-L60 — static std::string convert(const Eigen::Transform<Scalar, Dim, Mode, Options>& trafo)
- convert · function · L66-L70 — static std::string convert(const Eigen::Quaternion<Scalar, Options>& quat)
- make_cad_recipe · function · L152-L158 — static std::string make_cad_recipe()
- read_cad_recipe_entry · function · L164-L185 — static bool read_cad_recipe_entry(const std::string& path, std::string& out,
- rename_cad_recipe_entry_to_legacy · function · L193-L227 — static void rename_cad_recipe_entry_to_legacy(const std::string& path)
- out · function · L223-L223 — Zipper out(path);
