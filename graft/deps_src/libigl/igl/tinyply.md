# deps_src/libigl/igl/tinyply.h

- class · type · L44-L44 — enum class Type : uint8_t
- PropertyInfo · class · L57-L64 — struct PropertyInfo
- delete_array · class · L82-L82 — struct delete_array { void operator()(uint8_t * p) { delete[] p; } };
- data · function · L87-L87 — Buffer(const size_t size) : data(new uint8_t[size], delete_array()), size(size) { alias = data.get(); } // allocating
- size · function · L87-L87 — Buffer(const size_t size) : data(new uint8_t[size], delete_array()), size(size) { alias = data.get(); } // allocating
- get · function · L89-L89 — uint8_t * get() { return alias; }
- size_bytes · function · L90-L90 — size_t size_bytes() const { return size; }
- PlyData · class · L93-L97 — struct PlyData
- PlyProperty · class · L101-L108 — struct PlyProperty
- PlyElement · class · L114-L119 — struct PlyElement
- PlyFile · class · L123-L177 — struct PlyFile
