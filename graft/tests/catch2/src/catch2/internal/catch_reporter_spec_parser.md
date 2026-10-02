# tests/catch2/src/catch2/internal/catch_reporter_spec_parser.hpp

- ColourMode · type · L21-L21 — enum class ColourMode : std::uint8_t;
- splitReporterSpec · function · L25-L25 — std::vector<std::string> splitReporterSpec( StringRef reporterSpec );
- stringToColourMode · function · L27-L27 — Optional<ColourMode> stringToColourMode( StringRef colourMode );
- ReporterSpec · class · L38-L69 — class ReporterSpec
- ReporterSpec · function · L52-L56 — ReporterSpec(
- name · function · L58-L58 — std::string const& name() const { return m_name; }
- outputFile · function · L60-L60 — Optional<std::string> const& outputFile() const
- colourMode · function · L64-L64 — Optional<ColourMode> const& colourMode() const { return m_colourMode; }
- customOptions · function · L66-L66 — std::map<std::string, std::string> const& customOptions() const
- parseReporterSpec · function · L81-L81 — Optional<ReporterSpec> parseReporterSpec( StringRef reporterSpec );
