# tests/catch2/src/catch2/reporters/catch_reporter_registrars.hpp

- has_description · class · L24-L25 — template <typename T, typename = void>
- registerReporterImpl · function · L35-L36 — void registerReporterImpl( std::string const& name,
- registerListenerImpl · function · L38-L38 — void registerListenerImpl( Detail::unique_ptr<EventListenerFactory> listenerFactory );
- IEventListener · class · L41-L41 — class IEventListener;
- ReporterFactory · class · L44-L54 — template <typename T>
- create · function · L47-L49 — IEventListenerPtr create( ReporterConfig&& config ) const override
- getDescription · function · L51-L53 — std::string getDescription() const override
- ReporterRegistrar · class · L57-L64 — template<typename T>
- ReporterRegistrar · function · L60-L63 — explicit ReporterRegistrar( std::string const& name )
- ListenerRegistrar · class · L66-L101 — template<typename T>
- TypedListenerFactory · class · L69-L95 — class TypedListenerFactory : public EventListenerFactory
- getDescriptionImpl · function · L72-L74 — std::string getDescriptionImpl( std::true_type ) const
- getDescriptionImpl · function · L76-L78 — std::string getDescriptionImpl( std::false_type ) const
- TypedListenerFactory · function · L81-L82 — TypedListenerFactory( StringRef listenerName ):
- create · function · L84-L86 — IEventListenerPtr create( IConfig const* config ) const override
- getName · function · L88-L90 — StringRef getName() const override
- getDescription · function · L92-L94 — std::string getDescription() const override
- ListenerRegistrar · function · L98-L100 — ListenerRegistrar(StringRef listenerName)
