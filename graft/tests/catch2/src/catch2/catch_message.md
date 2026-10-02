# tests/catch2/src/catch2/catch_message.hpp

- IResultCapture · class · L25-L25 — class IResultCapture;
- MessageStream · class · L27-L36 — struct MessageStream
- MessageBuilder · class · L38-L51 — struct MessageBuilder : MessageStream
- MessageBuilder · function · L39-L42 — MessageBuilder( StringRef macroName,
- ScopedMessage · class · L53-L62 — class ScopedMessage
- ScopedMessage · function · L55-L55 — explicit ScopedMessage( MessageBuilder&& builder );
- ScopedMessage · function · L56-L56 — ScopedMessage( ScopedMessage& duplicate ) = delete;
- ScopedMessage · function · L57-L57 — ScopedMessage( ScopedMessage&& old ) noexcept;
- Capturer · class · L64-L87 — class Capturer
- Capturer · function · L68-L68 — Capturer( StringRef macroName, SourceLineInfo const& lineInfo, ResultWas::OfType resultType, StringRef names );
- Capturer · function · L70-L70 — Capturer(Capturer const&) = delete;
- captureValue · function · L75-L75 — void captureValue( size_t index, std::string const& value );
- captureValues · function · L77-L80 — template<typename T>
- captureValues · function · L82-L86 — template<typename T, typename... Ts>
