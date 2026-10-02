# deps_src/pybind11/include/pybind11/typing.h

- PYBIND11_NAMESPACE_BEGIN · function · L26-L45 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- PYBIND11_NAMESPACE_BEGIN · function · L143-L158 — PYBIND11_NAMESPACE_END(typing)
- accumulate · function · L269-L272 — constexpr auto num_special_chars = std::accumulate(
- begin · function · L270-L270 — special_chars.begin(), special_chars.end(), (size_t) 0, [&v](auto acc, const char &c)
- end · function · L270-L270 — special_chars.begin(), special_chars.end(), (size_t) 0, [&v](auto acc, const char &c)
- move · function · L271-L271 — return std::move(acc) + std::ranges::count(v, c);
- name · function · L275-L276 — for (auto c : StrLit.name)
- find · function · L276-L276 — if (special_chars.find(c) != std::string_view::npos)
- PYBIND11_NAMESPACE_END · function · L298-L298 — PYBIND11_NAMESPACE_END(PYBIND11_NAMESPACE)
