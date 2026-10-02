# src/libslic3r/Fill/FillHoneycomb.hpp

- FillHoneycomb · class · L12-L54 — class FillHoneycomb : public Fill
- is_self_crossing · function · L16-L16 — bool is_self_crossing() override { return false; }
- clone · function · L19-L19 — Fill* clone() const override { return new FillHoneycomb(*this); };
- _fill_surface_single · function · L20-L25 — void _fill_surface_single(
- CacheID · class · L28-L38 — struct CacheID
- CacheID · function · L30-L31 — CacheID(float adensity, coordf_t aspacing) :
- CacheData · class · L39-L49 — struct CacheData
- Cache · type · L50-L50 — typedef std::map<CacheID, CacheData> Cache;
- _layer_angle · function · L53-L53 — float _layer_angle(size_t idx) const override { return float(M_PI/3.) * (idx % 3); }
