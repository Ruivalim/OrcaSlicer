# tests/catch2/src/catch2/interfaces/catch_interfaces_enum_values_registry.hpp

- EnumInfo · class · L18-L25 — struct EnumInfo
- lookup · function · L24-L24 — StringRef lookup( int value ) const;
- IMutableEnumValuesRegistry · class · L28-L43 — class IMutableEnumValuesRegistry
- registerEnum · function · L32-L32 — virtual Detail::EnumInfo const& registerEnum( StringRef enumName, StringRef allEnums, std::vector<int> const& values ) = 0;
- registerEnum · function · L35-L35 — Detail::EnumInfo const& registerEnum( StringRef enumName, StringRef allEnums, std::initializer_list<E> values )
