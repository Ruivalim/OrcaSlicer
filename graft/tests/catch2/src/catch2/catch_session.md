# tests/catch2/src/catch2/catch_session.hpp

- Session · class · L27-L66 — class Session : Detail::NonCopyable
- Session · function · L30-L30 — Session();
- showHelp · function · L33-L33 — void showHelp() const;
- libIdentify · function · L34-L34 — void libIdentify();
- applyCommandLine · function · L36-L36 — int applyCommandLine( int argc, char const * const * argv );
- applyCommandLine · function · L38-L38 — int applyCommandLine( int argc, wchar_t const * const * argv );
- useConfigData · function · L41-L41 — void useConfigData( ConfigData const& configData );
- run · function · L43-L51 — template<typename CharT>
- run · function · L53-L53 — int run();
- cli · function · L55-L55 — Clara::Parser const& cli() const;
- cli · function · L56-L56 — void cli( Clara::Parser const& newParser );
- configData · function · L57-L57 — ConfigData& configData();
- config · function · L58-L58 — Config& config();
- runInternal · function · L60-L60 — int runInternal();
