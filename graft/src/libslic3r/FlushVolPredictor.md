# src/libslic3r/FlushVolPredictor.hpp

- RGBColor · class · L11-L18 — struct RGBColor
- RGBColor · function · L16-L16 — RGBColor(unsigned char r_,unsigned char g_,unsigned char b_) :r(r_),g(g_),b(b_){}
- RGBColor · function · L17-L17 — RGBColor() = default;
- LABColor · class · L20-L27 — struct LABColor
- LABColor · function · L25-L25 — LABColor() = default;
- LABColor · function · L26-L26 — LABColor(double l_,double a_,double b_):l(l_),a(a_),b(b_){}
- RGB2LAB · function · L29-L29 — LABColor RGB2LAB(const RGBColor& color);
- calc_color_distance · function · L31-L31 — float calc_color_distance(const LABColor& lab1, const LABColor& lab2);
- calc_color_distance · function · L32-L32 — float calc_color_distance(const RGBColor& rgb1, const RGBColor& rgb2);
- is_similar_color · function · L34-L34 — bool is_similar_color(const RGBColor& from, const RGBColor& to, float distance_threshold = 5.0);
- FlushVolPredictor · class · L38-L38 — class FlushVolPredictor;
- GenericFlushPredictor · class · L40-L49 — class GenericFlushPredictor
- GenericFlushPredictor · function · L44-L44 — explicit GenericFlushPredictor(const int dataset_value);
- predict · function · L45-L45 — bool predict(const RGB& from, const RGB& to, float& flush);
- get_min_flush_volume · function · L46-L46 — int get_min_flush_volume();
