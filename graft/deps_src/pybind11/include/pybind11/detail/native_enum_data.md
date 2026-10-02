# deps_src/pybind11/include/pybind11/detail/native_enum_data.h

- PYBIND11_NAMESPACE_BEGIN · function · L17-L17 — PYBIND11_NAMESPACE_BEGIN(detail)
- native_enum_missing_finalize_error_message · function · L21-L21 — native_enum_missing_finalize_error_message(const std::string &enum_name_encoded)
- parent_scope · function · L32-L37 — : enum_name_encoded{enum_name}, native_type_name_encoded{native_type_name},
- disarm_finalize_check · function · L52-L52 — void disarm_finalize_check(const char *error_context)
- arm_finalize_check · function · L60-L63 — void arm_finalize_check()
- global_internals_native_enum_type_map_set_item · function · L84-L88 — inline void global_internals_native_enum_type_map_set_item(const std::type_index &enum_type_index,
- global_internals_native_enum_type_map_get_item · function · L90-L99 — inline handle
- global_internals_native_enum_type_map_contains · function · L101-L106 — inline bool
- import_or_getattr · function · L108-L169 — inline object import_or_getattr(const std::string &fully_qualified_name,
- stream · function · L110-L110 — std::istringstream stream(fully_qualified_name);
- value_error · function · L118-L118 — throw value_error(msg);
- error_already_set · function · L128-L128 — throw error_already_set();
- value_error · function · L139-L139 — throw value_error(msg);
- c_str · function · L162-L162 — throw import_error(msg.c_str());
- import_error · function · L162-L162 — throw import_error(msg.c_str());
- finalize · function · L171-L197 — inline void native_enum_data::finalize()
- py_enum_type · function · L178-L178 — auto py_enum = py_enum_type(enum_name, members);
