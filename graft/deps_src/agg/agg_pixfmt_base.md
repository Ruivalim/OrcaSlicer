# deps_src/agg/agg_pixfmt_base.h

- pixfmt_gray_tag · class · L25-L27 — struct pixfmt_gray_tag
- pixfmt_rgb_tag · class · L29-L31 — struct pixfmt_rgb_tag
- pixfmt_rgba_tag · class · L33-L35 — struct pixfmt_rgba_tag
- color_type · type · L41-L41 — typedef ColorT color_type;
- order_type · type · L42-L42 — typedef Order order_type;
- value_type · type · L43-L43 — typedef typename color_type::value_type value_type;
- get · function · L45-L67 — static rgba get(value_type r, value_type g, value_type b, value_type a, cover_type cover = cover_full)
- c · function · L49-L53 — rgba c(
- to_double · function · L50-L50 — color_type::to_double(r),
- to_double · function · L51-L51 — color_type::to_double(g),
- to_double · function · L52-L52 — color_type::to_double(b),
- to_double · function · L53-L53 — color_type::to_double(a));
- get · function · L69-L77 — static rgba get(const value_type* p, cover_type cover = cover_full)
- set · function · L79-L85 — static void set(value_type* p, value_type r, value_type g, value_type b, value_type a)
- set · function · L87-L93 — static void set(value_type* p, const rgba& c)
