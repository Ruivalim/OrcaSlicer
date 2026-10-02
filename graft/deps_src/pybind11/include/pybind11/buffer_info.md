# deps_src/pybind11/include/pybind11/buffer_info.h

- PYBIND11_NAMESPACE_BEGIN · function · L14-L26 — PYBIND11_NAMESPACE_BEGIN(PYBIND11_NAMESPACE)
- c_strides · function · L19-L19 — inline std::vector<ssize_t> c_strides(const std::vector<ssize_t> &shape, ssize_t itemsize)
- f_strides · function · L31-L38 — inline std::vector<ssize_t> f_strides(const std::vector<ssize_t> &shape, ssize_t itemsize)
- move · function · L68-L68 — shape(std::move(shape_in)), strides(std::move(strides_in)), readonly(readonly)
- move · function · L68-L68 — shape(std::move(shape_in)), strides(std::move(strides_in)), readonly(readonly)
- size · function · L69-L69 — if (ndim != (ssize_t) shape.size() || ndim != (ssize_t) strides.size())
- buffer_info · function · L107-L107 — explicit buffer_info(Py_buffer *view, bool ownview = true)
- view · function · L153-L153 — Py_buffer *view() const { return m_view; }
- private_ctr_tag · class · L168-L181 — struct private_ctr_tag {};
- buffer_info · function · L170-L179 — buffer_info(private_ctr_tag,
- compare · function · L189-L189 — static bool compare(const buffer_info &b)
- format · function · L191-L191 — return b.format == format_descriptor<T>::format() && b.itemsize == (ssize_t) sizeof(T);
- compare · function · L197-L197 — static bool compare(const buffer_info &b)
- value · function · L199-L200 — && (b.format == format_descriptor<T>::value
- PYBIND11_NAMESPACE_END · function · L207-L208 — PYBIND11_NAMESPACE_END(detail)
