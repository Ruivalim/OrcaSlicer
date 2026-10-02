# tests/catch2/src/catch2/reporters/catch_reporter_tap.hpp

- TAPReporter · class · L16-L39 — class TAPReporter final : public StreamingReporterBase
- TAPReporter · function · L18-L22 — TAPReporter( ReporterConfig&& config ):
- getDescription · function · L24-L27 — static std::string getDescription()
- testRunStarting · function · L29-L29 — void testRunStarting( TestRunInfo const& testInfo ) override;
- noMatchingTestCases · function · L31-L31 — void noMatchingTestCases( StringRef unmatchedSpec ) override;
- assertionEnded · function · L33-L33 — void assertionEnded(AssertionStats const& _assertionStats) override;
- testRunEnded · function · L35-L35 — void testRunEnded(TestRunStats const& _testRunStats) override;
