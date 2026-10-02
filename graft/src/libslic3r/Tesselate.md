# src/libslic3r/Tesselate.hpp

- ExPolygon · class · L10-L10 — class ExPolygon;
- ExPolygons · type · L11-L11 — typedef std::vector<ExPolygon> ExPolygons;
- triangulate_expolygon_3d · function · L16-L16 — extern std::vector<Vec3d> triangulate_expolygon_3d (const ExPolygon  &poly,  coordf_t z = 0, bool flip = NORMALS_UP);
- triangulate_expolygons_3d · function · L17-L17 — extern std::vector<Vec3d> triangulate_expolygons_3d(const ExPolygons &polys, coordf_t z = 0, bool flip = NORMALS_UP);
- triangulate_expolygon_2d · function · L18-L18 — extern std::vector<Vec2d> triangulate_expolygon_2d (const ExPolygon  &poly,  bool flip = NORMALS_UP);
- triangulate_expolygons_2d · function · L19-L19 — extern std::vector<Vec2d> triangulate_expolygons_2d(const ExPolygons &polys, bool flip = NORMALS_UP);
- triangulate_expolygon_2f · function · L20-L20 — extern std::vector<Vec2f> triangulate_expolygon_2f (const ExPolygon  &poly,  bool flip = NORMALS_UP);
- triangulate_expolygons_2f · function · L21-L21 — extern std::vector<Vec2f> triangulate_expolygons_2f(const ExPolygons &polys, bool flip = NORMALS_UP);
