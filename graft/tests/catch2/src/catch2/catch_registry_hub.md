# tests/catch2/src/catch2/catch_registry_hub.cpp

- RegistryHub · class · L30-L86 — class RegistryHub : public IRegistryHub,
- RegistryHub · function · L35-L35 — RegistryHub() = default;
- getReporterRegistry · function · L36-L36 — ReporterRegistry const& getReporterRegistry() const override
- getTestCaseRegistry · function · L39-L39 — ITestCaseRegistry const& getTestCaseRegistry() const override
- getExceptionTranslatorRegistry · function · L42-L42 — IExceptionTranslatorRegistry const& getExceptionTranslatorRegistry() const override
- getTagAliasRegistry · function · L45-L45 — ITagAliasRegistry const& getTagAliasRegistry() const override
- getStartupExceptionRegistry · function · L48-L48 — StartupExceptionRegistry const& getStartupExceptionRegistry() const override
- registerReporter · function · L53-L55 — void registerReporter( std::string const& name, IReporterFactoryPtr factory ) override
- registerListener · function · L56-L58 — void registerListener( Detail::unique_ptr<EventListenerFactory> factory ) override
- registerTest · function · L59-L61 — void registerTest( Detail::unique_ptr<TestCaseInfo>&& testInfo, Detail::unique_ptr<ITestInvoker>&& invoker ) override
- registerTranslator · function · L62-L64 — void registerTranslator( Detail::unique_ptr<IExceptionTranslator>&& translator ) override
- registerTagAlias · function · L65-L67 — void registerTagAlias( std::string const& alias, std::string const& tag, SourceLineInfo const& lineInfo ) override
- registerStartupException · function · L68-L74 — void registerStartupException() noexcept override
- getMutableEnumValuesRegistry · function · L75-L75 — IMutableEnumValuesRegistry& getMutableEnumValuesRegistry() override
- getRegistryHub · function · L91-L91 — IRegistryHub const& getRegistryHub()
- getMutableRegistryHub · function · L94-L94 — IMutableRegistryHub& getMutableRegistryHub()
- cleanUp · function · L97-L99 — void cleanUp()
- translateActiveException · function · L100-L102 — std::string translateActiveException()
