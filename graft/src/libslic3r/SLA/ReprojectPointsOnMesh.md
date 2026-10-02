# src/libslic3r/SLA/ReprojectPointsOnMesh.hpp

- pos · function · L14-L14 — template<class Pt> Vec3d pos(const Pt &p) { return p.pos.template cast<double>(); }
- pos · function · L15-L15 — template<class Pt> void pos(Pt &p, const Vec3d &pp) { p.pos = pp.cast<float>(); }
- reproject_support_points · function · L17-L26 — template<class PointType>
- reproject_points_and_holes · function · L28-L43 — inline void reproject_points_and_holes(ModelObject *object)
