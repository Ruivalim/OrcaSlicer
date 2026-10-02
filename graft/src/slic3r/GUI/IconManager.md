# src/slic3r/GUI/IconManager.hpp

- IconManager · class · L16-L102 — class IconManager
- RasterType · type · L28-L34 — enum class RasterType: int
- InitType · class · L36-L46 — struct InitType
- Icon · class · L52-L64 — struct Icon
- is_valid · function · L62-L62 — bool is_valid() const { return tex_id != 0;}
- init · function · L76-L76 — Icons init(const InitTypes &input);
- init · function · L88-L88 — VIcons init(const std::vector<std::string> &file_paths, const ImVec2 &size, RasterType type = RasterType::color);
- release · function · L94-L94 — void release();
- draw · function · L111-L114 — void draw(const IconManager::Icon &icon,
- clickable · function · L122-L122 — bool clickable(const IconManager::Icon &icon, const IconManager::Icon &icon_hover);
- button · function · L131-L131 — bool button(const IconManager::Icon &activ, const IconManager::Icon &hover, const IconManager::Icon &disable, bool disabled = false);
