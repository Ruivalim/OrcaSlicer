# src/libslic3r/Zipper.hpp

- Zipper · class · L11-L88 — class Zipper
- e_compression · type · L14-L18 — enum e_compression
- Impl · class · L21-L21 — class Impl;
- Zipper · function · L30-L31 — explicit Zipper(const std::string& zipfname,
- Zipper · function · L35-L35 — Zipper(const Zipper&) = delete;
- Zipper · function · L42-L42 — Zipper(Zipper &&m);
- add_entry · function · L48-L48 — void add_entry(const std::string& name);
- add_entry · function · L52-L52 — void add_entry(const std::string& name, const void* data, size_t bytes);
- finish_entry · function · L83-L83 — void finish_entry();
- finalize · function · L85-L85 — void finalize();
- get_filename · function · L87-L87 — const std::string & get_filename() const;
