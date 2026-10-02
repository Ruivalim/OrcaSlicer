# src/slic3r/GUI/PluginSort.hpp

- PluginSortKey · type · L16-L25 — enum class PluginSortKey
- PluginSortOrder · type · L27-L31 — enum class PluginSortOrder
- to_string · function · L33-L45 — inline std::string to_string(PluginSortKey sort_key)
- to_string · function · L47-L50 — inline std::string to_string(PluginSortOrder sort_order)
- plugin_sort_key_from_string · function · L52-L65 — inline PluginSortKey plugin_sort_key_from_string(const std::string& sort_key, PluginSortKey fallback)
- plugin_sort_order_from_string · function · L67-L74 — inline PluginSortOrder plugin_sort_order_from_string(const std::string& sort_order, PluginSortOrder fallback)
- compare_ascii_case_insensitive_natural · function · L83-L130 — inline int compare_ascii_case_insensitive_natural(const std::string& lhs, const std::string& rhs)
- compare_plugin_base_order · function · L136-L148 — template <class PluginItem>
- compare_plugin_version · function · L154-L165 — inline int compare_plugin_version(const std::string& lhs, const std::string& rhs)
- compare_plugin_sort_key · function · L171-L192 — template <class PluginItem>
- sort_plugin_items_for_dialog · function · L197-L209 — template <class PluginItem>
