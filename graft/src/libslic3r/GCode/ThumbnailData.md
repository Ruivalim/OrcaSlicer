# src/libslic3r/GCode/ThumbnailData.hpp

- ThumbnailData · class · L13-L28 — struct ThumbnailData
- ThumbnailData · function · L19-L19 — ThumbnailData() { reset(); }
- set · function · L20-L20 — void set(unsigned int w, unsigned int h);
- reset · function · L21-L21 — void reset();
- is_valid · function · L23-L23 — bool is_valid() const;
- load_from · function · L24-L27 — void load_from(ThumbnailData &data)
- ThumbnailsParams · class · L33-L42 — struct ThumbnailsParams
- ThumbnailsGeneratorCallback · type · L44-L44 — typedef std::function<ThumbnailsList(const ThumbnailsParams&)> ThumbnailsGeneratorCallback;
- BBoxData · class · L46-L69 — struct BBoxData
- to_json · function · L53-L61 — void to_json(nlohmann::json& j) const
- from_json · function · L62-L68 — void from_json(const nlohmann::json& j)
- PlateBBoxData · class · L71-L120 — struct PlateBBoxData
- to_json · function · L86-L101 — void to_json(nlohmann::json& j) const
- from_json · function · L102-L116 — void from_json(const nlohmann::json& j)
- is_valid · function · L117-L119 — bool is_valid() const
