# tests/catch2/src/catch2/interfaces/catch_interfaces_testcase.hpp

- TestCaseHandle · class · L16-L16 — class TestCaseHandle;
- IConfig · class · L17-L17 — class IConfig;
- ITestCaseRegistry · class · L19-L26 — class ITestCaseRegistry
- getAllInfos · function · L23-L23 — virtual std::vector<TestCaseInfo* > const& getAllInfos() const = 0;
- getAllTests · function · L24-L24 — virtual std::vector<TestCaseHandle> const& getAllTests() const = 0;
- getAllTestsSorted · function · L25-L25 — virtual std::vector<TestCaseHandle> const& getAllTestsSorted( IConfig const& config ) const = 0;
