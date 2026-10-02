# tests/catch2/src/catch2/reporters/catch_reporter_compact.hpp

- CompactReporter · class · L17-L38 — class CompactReporter final : public StreamingReporterBase
- CompactReporter · function · L19-L22 — CompactReporter( ReporterConfig&& _config ):
- getDescription · function · L26-L26 — static std::string getDescription();
- noMatchingTestCases · function · L28-L28 — void noMatchingTestCases( StringRef unmatchedSpec ) override;
- testRunStarting · function · L30-L30 — void testRunStarting( TestRunInfo const& _testInfo ) override;
- assertionEnded · function · L32-L32 — void assertionEnded(AssertionStats const& _assertionStats) override;
- sectionEnded · function · L34-L34 — void sectionEnded(SectionStats const& _sectionStats) override;
- testRunEnded · function · L36-L36 — void testRunEnded(TestRunStats const& _testRunStats) override;
