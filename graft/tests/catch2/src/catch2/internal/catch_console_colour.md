# tests/catch2/src/catch2/internal/catch_console_colour.hpp

- ColourMode · type · L18-L18 — enum class ColourMode : std::uint8_t;
- IStream · class · L19-L19 — class IStream;
- Colour · class · L21-L58 — struct Colour
- Code · type · L22-L57 — enum Code
- ColourImpl · class · L60-L130 — class ColourImpl
- ColourImpl · function · L65-L65 — ColourImpl( IStream* stream ): m_stream( stream ) {}
- ColourGuard · class · L69-L117 — class ColourGuard
- ColourGuard · function · L76-L77 — ColourGuard( Colour::Code code,
- ColourGuard · function · L79-L79 — ColourGuard( ColourGuard const& rhs ) = delete;
- ColourGuard · function · L82-L82 — ColourGuard( ColourGuard&& rhs ) noexcept;
- engage · function · L93-L93 — ColourGuard& engage( std::ostream& stream ) &;
- engage · function · L99-L99 — ColourGuard&& engage( std::ostream& stream ) &&;
- engageImpl · function · L115-L115 — void engageImpl( std::ostream& stream );
- guardColour · function · L126-L126 — ColourGuard guardColour( Colour::Code colourCode );
- use · function · L129-L129 — virtual void use( Colour::Code colourCode ) const = 0;
- makeColourImpl · function · L133-L134 — Detail::unique_ptr<ColourImpl> makeColourImpl( ColourMode colourSelection,
- isColourImplAvailable · function · L137-L137 — bool isColourImplAvailable( ColourMode colourSelection );
