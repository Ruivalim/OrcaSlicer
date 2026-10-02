# src/libvgcode/src/Bitset.hpp

- BitSet · class · L19-L99 — template<typename T = unsigned long long>
- BitSet · function · L22-L22 — BitSet() = default;
- BitSet · function · L23-L23 — BitSet(std::size_t size) : size(size), blocks(1 + (size / (sizeof(T) * 8))) { clear(); }
- clear · function · L25-L29 — void clear()
- setAll · function · L31-L35 — void setAll()
- set · function · L38-L44 — bool set(std::size_t index)
- reset · function · L47-L53 — bool reset(std::size_t index)
- set_atomic · function · L70-L76 — template<typename U = T>
- reset_atomic · function · L79-L85 — template<typename U = T>
- get_coords · function · L87-L91 — std::pair<std::size_t, std::size_t> get_coords(std::size_t index) const
- size_in_bytes_cpu · function · L93-L95 — std::size_t size_in_bytes_cpu() const
