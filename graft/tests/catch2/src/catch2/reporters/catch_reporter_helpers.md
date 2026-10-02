# tests/catch2/src/catch2/reporters/catch_reporter_helpers.hpp

- IConfig · class · L21-L21 — class IConfig;
- TestCaseHandle · class · L22-L22 — class TestCaseHandle;
- ColourImpl · class · L23-L23 — class ColourImpl;
- getFormattedDuration · function · L26-L26 — std::string getFormattedDuration( double duration );
- shouldShowDuration · function · L29-L29 — bool shouldShowDuration( IConfig const& config, double duration );
- serializeFilters · function · L31-L31 — std::string serializeFilters( std::vector<std::string> const& filters );
- lineOfChars · class · L33-L38 — struct lineOfChars
- lineOfChars · function · L35-L35 — constexpr lineOfChars( char c_ ): c( c_ ) {}
- defaultListReporters · function · L48-L51 — void
- defaultListListeners · function · L57-L58 — void defaultListListeners( std::ostream& out,
- defaultListTags · function · L67-L67 — void defaultListTags( std::ostream& out, std::vector<TagInfo> const& tags, bool isFiltered );
- defaultListTests · function · L78-L82 — void defaultListTests( std::ostream& out,
- printTestRunTotals · function · L89-L91 — void printTestRunTotals( std::ostream& stream,
