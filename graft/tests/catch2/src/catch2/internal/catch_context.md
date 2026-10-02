# tests/catch2/src/catch2/internal/catch_context.hpp

- IResultCapture · class · L15-L15 — class IResultCapture;
- IConfig · class · L16-L16 — class IConfig;
- Context · class · L18-L35 — class Context
- getCurrentMutableContext · function · L23-L23 — friend Context& getCurrentMutableContext();
- getCurrentContext · function · L24-L24 — friend Context const& getCurrentContext();
- getResultCapture · function · L27-L27 — constexpr IResultCapture* getResultCapture() const
- getConfig · function · L30-L30 — constexpr IConfig const* getConfig() const { return m_config; }
- setResultCapture · function · L31-L33 — constexpr void setResultCapture( IResultCapture* resultCapture )
- setConfig · function · L34-L34 — constexpr void setConfig( IConfig const* config ) { m_config = config; }
- getCurrentMutableContext · function · L37-L37 — Context& getCurrentMutableContext();
- getCurrentContext · function · L39-L39 — inline Context const& getCurrentContext()
- SimplePcg32 · class · L43-L43 — class SimplePcg32;
- sharedRng · function · L44-L44 — SimplePcg32& sharedRng();
