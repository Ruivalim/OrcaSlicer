# src/libslic3r/Format/3mf.hpp

- PrusaFileParser · class · L7-L27 — class PrusaFileParser
- PrusaFileParser · function · L10-L10 — PrusaFileParser() {}
- check_3mf_from_prusa · function · L13-L13 — bool check_3mf_from_prusa(const std::string filename);
- _start_element_handler · function · L14-L14 — void _start_element_handler(const char *name, const char **attributes);
- _characters_handler · function · L15-L15 — void _characters_handler(const XML_Char *s, int len);
- get_attribute_value_charptr · function · L18-L18 — const char *get_attribute_value_charptr(const char **attributes, unsigned int attributes_size, const char *attribute_key);
- get_attribute_value_string · function · L19-L19 — std::string get_attribute_value_string(const char **attributes, unsigned int attributes_size, const char *attribute_key);
- start_element_handler · function · L21-L21 — static void XMLCALL start_element_handler(void *userData, const char *name, const char **attributes);
- characters_handler · function · L22-L22 — static void XMLCALL characters_handler(void *userData, const XML_Char *s, int len);
- Model · class · L50-L50 — class Model;
- DynamicPrintConfig · class · L52-L52 — class DynamicPrintConfig;
- load_3mf · function · L56-L56 — extern bool load_3mf(const char* path, DynamicPrintConfig& config, ConfigSubstitutionContext& config_substitutions, Model* model, bool check_version);
- store_3mf · function · L60-L60 — extern bool store_3mf(const char* path, Model* model, const DynamicPrintConfig* config, bool fullpath_sources, const ThumbnailData* thumbnail_data = nullptr, bool zip64 = true);
