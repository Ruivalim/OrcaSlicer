# tests/catch2/src/catch2/internal/catch_output_redirect.hpp

- OutputRedirect · class · L18-L49 — class OutputRedirect
- activateImpl · function · L20-L20 — virtual void activateImpl() = 0;
- deactivateImpl · function · L21-L21 — virtual void deactivateImpl() = 0;
- Kind · type · L23-L30 — enum Kind
- getStdout · function · L35-L35 — virtual std::string getStdout() = 0;
- getStderr · function · L36-L36 — virtual std::string getStderr() = 0;
- clearBuffers · function · L37-L37 — virtual void clearBuffers() = 0;
- isActive · function · L38-L38 — bool isActive() const { return m_redirectActive; }
- activate · function · L39-L43 — void activate()
- deactivate · function · L44-L48 — void deactivate()
- isRedirectAvailable · function · L51-L51 — bool isRedirectAvailable( OutputRedirect::Kind kind);
- makeOutputRedirect · function · L52-L52 — Detail::unique_ptr<OutputRedirect> makeOutputRedirect( bool actual );
- RedirectGuard · class · L54-L70 — class RedirectGuard
- RedirectGuard · function · L61-L61 — RedirectGuard( bool activate, OutputRedirect& redirectImpl );
- RedirectGuard · function · L64-L64 — RedirectGuard( RedirectGuard const& ) = delete;
- RedirectGuard · function · L68-L68 — RedirectGuard( RedirectGuard&& rhs ) noexcept;
- scopedActivate · function · L72-L72 — RedirectGuard scopedActivate( OutputRedirect& redirectImpl );
- scopedDeactivate · function · L73-L73 — RedirectGuard scopedDeactivate( OutputRedirect& redirectImpl );
