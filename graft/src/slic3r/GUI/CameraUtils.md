# src/slic3r/GUI/CameraUtils.hpp

- GLVolume · class · L7-L7 — class GLVolume;
- CameraUtils · class · L15-L66 — class CameraUtils
- CameraUtils · function · L18-L18 — CameraUtils() = delete; // only static functions
- project · function · L27-L27 — static Points project(const Camera& camera, const std::vector<Vec3d> &points);
- project · function · L28-L28 — static Slic3r::Point project(const Camera& camera, const Vec3d &point);
- create_hull2d · function · L36-L36 — static Polygon create_hull2d(const Camera &camera, const GLVolume &volume);
- ray_from_screen_pos · function · L45-L45 — static void ray_from_screen_pos(const Camera &camera, const Vec2d &position, Vec3d &point, Vec3d &direction);
- ray_from_ortho_screen_pos · function · L46-L46 — static void ray_from_ortho_screen_pos(const Camera &camera, const Vec2d &position, Vec3d &point, Vec3d &direction);
- ray_from_persp_screen_pos · function · L47-L47 — static void ray_from_persp_screen_pos(const Camera &camera, const Vec2d &position, Vec3d &point, Vec3d &direction);
- get_z0_position · function · L56-L56 — static Vec2d get_z0_position(const Camera &camera, const Vec2d &coor);
- screen_point · function · L64-L64 — static Vec3d screen_point(const Camera &camera, const Vec2d &position);
