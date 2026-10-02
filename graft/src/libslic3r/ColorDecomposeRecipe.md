# src/libslic3r/ColorDecomposeRecipe.hpp

- ColorDecomposeRecipeMode · type · L9-L13 — enum class ColorDecomposeRecipeMode
- ColorDecomposeRgb · class · L15-L19 — struct ColorDecomposeRgb
- ColorDecomposePhysicalFilament · class · L21-L27 — struct ColorDecomposePhysicalFilament
- ColorDecomposeRecipeComponent · class · L29-L34 — struct ColorDecomposeRecipeComponent
- ColorDecomposeRecipeResult · class · L36-L41 — struct ColorDecomposeRecipeResult
- color_decompose_rgb_to_hex · function · L43-L43 — std::string color_decompose_rgb_to_hex(const ColorDecomposeRgb& rgb);
- color_decompose_hex_to_rgb · function · L44-L44 — bool color_decompose_hex_to_rgb(const std::string& hex, ColorDecomposeRgb& out);
- recommend_from_physical_filaments · function · L46-L49 — ColorDecomposeRecipeResult recommend_from_physical_filaments(
- lookup_standard_recipe · function · L51-L54 — ColorDecomposeRecipeResult lookup_standard_recipe(
- lookup_measured_blend_color · function · L59-L60 — std::string lookup_measured_blend_color(const std::vector<std::string>& component_hexes,
