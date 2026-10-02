# tests/catch2/src/catch2/reporters/catch_reporter_teamcity.hpp

- TeamCityReporter · class · L23-L59 — class TeamCityReporter final : public StreamingReporterBase
- TeamCityReporter · function · L25-L30 — TeamCityReporter( ReporterConfig&& _config )
- getDescription · function · L34-L37 — static std::string getDescription()
- testRunStarting · function · L39-L39 — void testRunStarting( TestRunInfo const& runInfo ) override;
- testRunEnded · function · L40-L40 — void testRunEnded( TestRunStats const& runStats ) override;
- assertionEnded · function · L43-L43 — void assertionEnded(AssertionStats const& assertionStats) override;
- sectionStarting · function · L45-L48 — void sectionStarting(SectionInfo const& sectionInfo) override
- testCaseStarting · function · L50-L50 — void testCaseStarting(TestCaseInfo const& testInfo) override;
- testCaseEnded · function · L52-L52 — void testCaseEnded(TestCaseStats const& testCaseStats) override;
- printSectionHeader · function · L55-L55 — void printSectionHeader(std::ostream& os);
