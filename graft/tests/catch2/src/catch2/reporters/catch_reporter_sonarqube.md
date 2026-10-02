# tests/catch2/src/catch2/reporters/catch_reporter_sonarqube.hpp

- SonarQubeReporter · class · L18-L55 — class SonarQubeReporter final : public CumulativeReporterBase
- SonarQubeReporter · function · L20-L27 — SonarQubeReporter(ReporterConfig&& config)
- getDescription · function · L29-L32 — static std::string getDescription()
- testRunStarting · function · L34-L34 — void testRunStarting( TestRunInfo const& testRunInfo ) override;
- testRunEndedCumulative · function · L36-L39 — void testRunEndedCumulative() override
- writeRun · function · L41-L41 — void writeRun( TestRunNode const& runNode );
- writeTestFile · function · L43-L43 — void writeTestFile(StringRef filename, std::vector<TestCaseNode const*> const& testCaseNodes);
- writeTestCase · function · L45-L45 — void writeTestCase(TestCaseNode const& testCaseNode);
- writeSection · function · L47-L47 — void writeSection(std::string const& rootName, SectionNode const& sectionNode, bool okToFail);
- writeAssertions · function · L49-L49 — void writeAssertions(SectionNode const& sectionNode, bool okToFail);
- writeAssertion · function · L51-L51 — void writeAssertion(AssertionStats const& stats, bool okToFail);
