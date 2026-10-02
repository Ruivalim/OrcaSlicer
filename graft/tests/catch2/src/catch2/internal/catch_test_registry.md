# tests/catch2/src/catch2/internal/catch_test_registry.hpp

- TestInvokerAsMethod · class · L31-L42 — template<typename C>
- TestInvokerAsMethod · function · L35-L36 — constexpr TestInvokerAsMethod( void ( C::*testAsMethod )() ) noexcept:
- invoke · function · L38-L41 — void invoke() const override
- makeTestInvoker · function · L46-L49 — template<typename C>
- TestInvokerFixture · class · L51-L72 — template <typename C>
- TestInvokerFixture · function · L57-L58 — constexpr TestInvokerFixture( void ( C::*testAsMethod )() const ) noexcept:
- prepareTestCase · function · L60-L62 — void prepareTestCase() override
- tearDownTestCase · function · L64-L66 — void tearDownTestCase() override
- invoke · function · L68-L71 — void invoke() const override
- makeTestInvokerFixture · function · L74-L77 — template<typename C>
- NameAndTags · class · L79-L85 — struct NameAndTags
- NameAndTags · function · L80-L82 — constexpr NameAndTags( StringRef name_ = StringRef(),
- AutoReg · class · L87-L89 — struct AutoReg : Detail::NonCopyable
- AutoReg · function · L88-L88 — AutoReg( Detail::unique_ptr<ITestInvoker> invoker, SourceLineInfo const& lineInfo, StringRef classOrMethod, NameAndTags const& nameAndTags ) noexcept;
- INTERNAL_CATCH_TESTCASE · function · L117-L117 — #define INTERNAL_CATCH_TESTCASE( ... ) \
- DummyUse · class · L126-L128 — struct DummyUse
- DummyUse · function · L127-L127 — DummyUse( void ( * )( int ), Catch::NameAndTags const& );
