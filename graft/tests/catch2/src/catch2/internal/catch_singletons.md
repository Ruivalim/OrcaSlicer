# tests/catch2/src/catch2/internal/catch_singletons.hpp

- ISingleton · class · L13-L15 — struct ISingleton
- addSingleton · function · L18-L18 — void addSingleton( ISingleton* singleton );
- cleanupSingletons · function · L19-L19 — void cleanupSingletons();
- Singleton · class · L22-L41 — template<typename SingletonImplT, typename InterfaceT = SingletonImplT, typename MutableInterfaceT = InterfaceT>
- getInternal · function · L25-L32 — static auto getInternal() -> Singleton*
- get · function · L35-L37 — static auto get() -> InterfaceT const&
- getMutable · function · L38-L40 — static auto getMutable() -> MutableInterfaceT&
