# src/libslic3r/Orient.hpp

- OrientMesh · class · L25-L49 — struct OrientMesh
- apply · function · L47-L47 — void apply() const { if (setter) setter(*this); }
- OrientParams · class · L51-L97 — struct OrientParams
- OrientParams · function · L96-L96 — OrientParams() = default;
- orient · function · L108-L108 — void orient(OrientMeshs &items, const OrientMeshs &excludes, const OrientParams &params = {});
- orient · function · L111-L111 — void orient(ModelObject* obj);
- orient · function · L113-L113 — void orient(ModelInstance* instance);
- orient_for_cooling · function · L116-L116 — void orient_for_cooling(TriangleMesh& mesh, const FanDirection& fan_dir);
