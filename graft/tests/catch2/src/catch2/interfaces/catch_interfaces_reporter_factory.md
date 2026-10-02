# tests/catch2/src/catch2/interfaces/catch_interfaces_reporter_factory.hpp

- IConfig · class · L19-L19 — class IConfig;
- IEventListener · class · L20-L20 — class IEventListener;
- IReporterFactory · class · L24-L31 — class IReporterFactory
- create · function · L28-L29 — virtual IEventListenerPtr
- getDescription · function · L30-L30 — virtual std::string getDescription() const = 0;
- EventListenerFactory · class · L34-L42 — class EventListenerFactory
- create · function · L37-L37 — virtual IEventListenerPtr create( IConfig const* config ) const = 0;
- getName · function · L39-L39 — virtual StringRef getName() const = 0;
- getDescription · function · L41-L41 — virtual std::string getDescription() const = 0;
