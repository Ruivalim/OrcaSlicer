# src/libslic3r/Exception.hpp

- Exception · class · L11-L11 — class Exception : public std::runtime_error { using std::runtime_error::runtime_error; };
- SlicingError · class · L29-L38 — class SlicingError : public Exception
- SlicingError · function · L33-L33 — SlicingError(std::string const &msg, size_t objectId) : Exception(msg), objectId_(objectId) {}
- objectId · function · L34-L34 — size_t objectId() const { return objectId_; }
- SlicingErrors · class · L40-L47 — class SlicingErrors : public Exception
- SlicingErrors · function · L44-L44 — SlicingErrors(const std::vector<SlicingError> &errors) : Exception("Errors"), errors_(errors) {}
