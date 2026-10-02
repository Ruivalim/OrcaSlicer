# src/slic3r/plugin/PyPluginTrampoline.hpp

- PyPluginCommonTrampoline · class · L59-L140 — template<class Base> class PyPluginCommonTrampoline : public Base
- get_name · function · L64-L67 — std::string get_name() const override
- has_config_ui · function · L71-L79 — bool has_config_ui() const override
- get_config_ui · function · L81-L89 — std::string get_config_ui() const override
- get_default_config · function · L98-L119 — nlohmann::json get_default_config() const override
- on_load · function · L121-L124 — void on_load() override
- on_unload · function · L126-L129 — void on_unload() override
- on_cancelled · function · L131-L134 — void on_cancelled() override
- on_lifecycle_event · function · L136-L139 — void on_lifecycle_event(LifecycleEvent event, const LifecycleEventContext& ctx) override
- PyPluginInterfaceTrampoline · class · L142-L153 — class PyPluginInterfaceTrampoline : public PyPluginCommonTrampoline<PluginCapabilityInterface>
- get_type · function · L147-L152 — PluginCapabilityType get_type() const override
