# src/slic3r/plugin/pluginTypes/script/ScriptPluginCapability.hpp

- ScriptPluginCapability · class · L7-L15 — class ScriptPluginCapability : public PluginCapabilityInterface
- get_type · function · L10-L10 — PluginCapabilityType get_type() const override { return PluginCapabilityType::Script; }
- execute · function · L12-L12 — virtual ExecutionResult execute() = 0;
- RegisterBindings · function · L14-L14 — static void RegisterBindings(pybind11::module_ &module);
