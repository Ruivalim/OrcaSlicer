# tests/catch2/src/catch2/internal/catch_test_case_registry_impl.hpp

- IConfig · class · L19-L19 — class IConfig;
- ITestInvoker · class · L20-L20 — class ITestInvoker;
- TestCaseHandle · class · L21-L21 — class TestCaseHandle;
- TestSpec · class · L22-L22 — class TestSpec;
- sortTests · function · L24-L24 — std::vector<TestCaseHandle> sortTests( IConfig const& config, std::vector<TestCaseHandle> const& unsortedTestCases );
- isThrowSafe · function · L26-L26 — bool isThrowSafe( TestCaseHandle const& testCase, IConfig const& config );
- filterTests · function · L28-L28 — std::vector<TestCaseHandle> filterTests( std::vector<TestCaseHandle> const& testCases, TestSpec const& testSpec, IConfig const& config );
- getAllTestCasesSorted · function · L29-L29 — std::vector<TestCaseHandle> const& getAllTestCasesSorted( IConfig const& config );
- TestRegistry · class · L31-L51 — class TestRegistry : public ITestCaseRegistry
- registerTest · function · L33-L33 — void registerTest( Detail::unique_ptr<TestCaseInfo> testInfo, Detail::unique_ptr<ITestInvoker> testInvoker );
- getAllInfos · function · L35-L35 — std::vector<TestCaseInfo*> const& getAllInfos() const override;
- getAllTests · function · L36-L36 — std::vector<TestCaseHandle> const& getAllTests() const override;
- getAllTestsSorted · function · L37-L37 — std::vector<TestCaseHandle> const& getAllTestsSorted( IConfig const& config ) const override;
