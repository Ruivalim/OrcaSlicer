# tests/catch2/src/catch2/internal/catch_assertion_handler.hpp

- AssertionReaction · class · L19-L23 — struct AssertionReaction
- AssertionHandler · class · L25-L62 — class AssertionHandler
- AssertionHandler · function · L32-L36 — AssertionHandler
- handleExpr · function · L44-L47 — template<typename T>
- handleExpr · function · L48-L48 — void handleExpr( ITransientExpression const& expr );
- handleMessage · function · L50-L50 — void handleMessage(ResultWas::OfType resultType, std::string&& message);
- handleExceptionThrownAsExpected · function · L52-L52 — void handleExceptionThrownAsExpected();
- handleUnexpectedExceptionNotThrown · function · L53-L53 — void handleUnexpectedExceptionNotThrown();
- handleExceptionNotThrownAsExpected · function · L54-L54 — void handleExceptionNotThrownAsExpected();
- handleThrowingCallSkipped · function · L55-L55 — void handleThrowingCallSkipped();
- handleUnexpectedInflightException · function · L56-L56 — void handleUnexpectedInflightException();
- complete · function · L58-L58 — void complete();
- allowThrows · function · L61-L61 — auto allowThrows() const -> bool;
- handleExceptionMatchExpr · function · L64-L64 — void handleExceptionMatchExpr( AssertionHandler& handler, std::string const& str );
