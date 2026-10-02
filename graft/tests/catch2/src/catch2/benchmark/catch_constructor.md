# tests/catch2/src/catch2/benchmark/catch_constructor.hpp

- ObjectStorage · class · L20-L57 — template <typename T, bool Destruct>
- ObjectStorage · function · L23-L23 — ObjectStorage() = default;
- ObjectStorage · function · L25-L28 — ObjectStorage(const ObjectStorage& other)
- ObjectStorage · function · L30-L33 — ObjectStorage(ObjectStorage&& other)
- construct · function · L37-L41 — template <typename... Args>
- destruct · function · L43-L47 — template <bool AllowManualDestruction = !Destruct>
- stored_object · function · L61-L61 — T& stored_object() { return *reinterpret_cast<T*>( data ); }
- stored_object · function · L63-L63 — T const& stored_object() const
