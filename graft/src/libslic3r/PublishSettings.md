# src/libslic3r/PublishSettings.hpp

- PresetBundle · class · L7-L7 — class PresetBundle;
- publish_base_key · function · L10-L10 — std::string publish_base_key(const std::string &key);
- publish_structural_keys · function · L16-L16 — const std::set<std::string>& publish_structural_keys();
- publish_mixed_keys · function · L20-L20 — const std::set<std::string>& publish_mixed_keys();
- PublishablePrinterOption · class · L23-L26 — struct PublishablePrinterOption
- publishable_printer_retraction_options · function · L29-L29 — const std::vector<PublishablePrinterOption>& publishable_printer_retraction_options();
- publishable_printer_z_hop_options · function · L30-L30 — const std::vector<PublishablePrinterOption>& publishable_printer_z_hop_options();
- publishable_printer_keys · function · L34-L34 — const std::set<std::string>& publishable_printer_keys();
- collect_dirty_settings_keys · function · L38-L38 — std::vector<std::string> collect_dirty_settings_keys(const PresetBundle& bundle);
- PublishedMaterialEntry · class · L44-L79 — struct PublishedMaterialEntry
- normalize_filament_type · function · L82-L82 — std::string normalize_filament_type(const std::string& type);
- DynamicPrintConfig · class · L84-L84 — class DynamicPrintConfig;
- make_publish_universal · function · L87-L87 — void make_publish_universal(DynamicPrintConfig &config);
- publish_material_base_name · function · L91-L91 — std::string publish_material_base_name(const std::string &preset_name);
- filter_published_config · function · L95-L98 — DynamicPrintConfig filter_published_config(
