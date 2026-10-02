# src/libslic3r/LifecycleEvents.hpp

- LifecycleEvent · type · L19-L64 — enum class LifecycleEvent
- LifecycleEvtCode · type · L68-L68 — enum class LifecycleEvtCode { Ok, Error, Warn };
- LifecycleEventContext · class · L70-L111 — struct LifecycleEventContext
- lifecycle_event_to_string · function · L113-L156 — inline std::string lifecycle_event_to_string(LifecycleEvent event)
- lifecycle_evt_code_to_string · function · L158-L166 — inline std::string lifecycle_evt_code_to_string(LifecycleEvtCode code)
- LifecycleHookState · class · L176-L183 — struct LifecycleHookState
- lifecycle_hook_state · function · L185-L185 — inline LifecycleHookState& lifecycle_hook_state()
- LifecycleDispatchGuard · class · L191-L209 — class LifecycleDispatchGuard
- LifecycleDispatchGuard · function · L194-L194 — explicit LifecycleDispatchGuard(LifecycleHookState& state) : m_state(state) {}
- LifecycleDispatchGuard · function · L204-L204 — LifecycleDispatchGuard(const LifecycleDispatchGuard&)            = delete;
- set_lifecycle_hook_fn · function · L218-L232 — inline void set_lifecycle_hook_fn(LifecycleHookFn fn)
- fire_lifecycle_event · function · L234-L248 — inline void fire_lifecycle_event(LifecycleEvent event, const LifecycleEventContext& ctx)
- guard · function · L246-L246 — detail::LifecycleDispatchGuard guard(state);
