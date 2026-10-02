# deps_src/libnest2d/tools/svgtools.hpp

- SVGWriter · class · L13-L170 — template<class RawShape>
- OrigoLocation · type · L22-L25 — enum OrigoLocation
- Config · class · L27-L36 — struct Config
- Config · function · L32-L34 — Config():
- SVGWriter · function · L45-L46 — SVGWriter(const Config& conf = Config()):
- setSize · function · L48-L55 — void setSize(const Box &box)
- writeShape · function · L57-L80 — void writeShape(RawShape tsh, std::string fill = "none", std::string stroke = "black", float stroke_width = 1)
- writeItem · function · L82-L84 — void writeItem(const Item& item, std::string fill = "none", std::string stroke = "black", float stroke_width = 1)
- writePackGroup · function · L86-L94 — void writePackGroup(const PackGroup& result)
- writeItems · function · L96-L106 — template<class ItemIt> void writeItems(ItemIt from, ItemIt to)
- draw_text · function · L108-L115 — void draw_text(float x,float y, const std::string text, const std::string color, int font_size)
- addLayer · function · L117-L120 — void addLayer()
- finishLayer · function · L122-L125 — void finishLayer()
- save · function · L127-L138 — void save(const std::string& filepath)
- save · function · L141-L154 — void save(const boost::filesystem::path &filepath)
- currentLayer · function · L158-L158 — std::string& currentLayer() { return svg_layers_.back(); }
- header · function · L160-L168 — const std::string header() const
