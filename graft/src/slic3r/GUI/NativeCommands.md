# src/slic3r/GUI/NativeCommands.hpp

- NativeCommand · class · L16-L24 — struct NativeCommand
- catalog · function · L29-L29 — const std::vector<NativeCommand>& catalog();
- rebuild_catalog · function · L32-L32 — void rebuild_catalog();
- run · function · L35-L35 — AppActionRunResult run(const std::string& key, const std::string& param = {});
- make_action · function · L40-L40 — std::unique_ptr<AppAction> make_action(const NativeCommand& command);
