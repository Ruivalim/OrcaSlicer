# tests/libslic3r/test_lay_on_face.cpp

- add_box · function · L12-L17 — void add_box(ModelObject &object, const Vec3d &size, const Vec3d &origin = Vec3d::Zero())
- add_box_object · function · L19-L19 — ModelObject &add_box_object(Model &model, const Vec3d &size)
- add_ribbed_plate · function · L29-L29 — ModelObject &add_ribbed_plate(Model &model)
- instance_planes · function · L39-L42 — std::vector<LayOnFacePlane> instance_planes(const ModelObject &object)
- lay_on_largest_face · function · L44-L50 — void lay_on_largest_face(ModelObject &object)
- check_size · function · L52-L58 — void check_size(const ModelObject &object, const Vec3d &expected)
- check_on_bed · function · L60-L60 — void check_on_bed(const ModelObject &object) { CHECK_THAT(object.instance_bounding_box(0).min.z(), WithinAbs(0., 1e-3)); }
