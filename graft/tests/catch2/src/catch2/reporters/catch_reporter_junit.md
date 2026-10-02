# tests/catch2/src/catch2/reporters/catch_reporter_junit.hpp

- JunitReporter · class · L18-L52 — class JunitReporter final : public CumulativeReporterBase
- JunitReporter · function · L20-L20 — JunitReporter(ReporterConfig&& _config);
- getDescription · function · L22-L22 — static std::string getDescription();
- testRunStarting · function · L24-L24 — void testRunStarting(TestRunInfo const& runInfo) override;
- testCaseStarting · function · L26-L26 — void testCaseStarting(TestCaseInfo const& testCaseInfo) override;
- assertionEnded · function · L27-L27 — void assertionEnded(AssertionStats const& assertionStats) override;
- testCaseEnded · function · L29-L29 — void testCaseEnded(TestCaseStats const& testCaseStats) override;
- testRunEndedCumulative · function · L31-L31 — void testRunEndedCumulative() override;
- writeRun · function · L34-L34 — void writeRun(TestRunNode const& testRunNode, double suiteTime);
- writeTestCase · function · L36-L36 — void writeTestCase(TestCaseNode const& testCaseNode);
- writeSection · function · L38-L41 — void writeSection( std::string const& className,
- writeAssertions · function · L43-L43 — void writeAssertions(SectionNode const& sectionNode);
- writeAssertion · function · L44-L44 — void writeAssertion(AssertionStats const& stats);
