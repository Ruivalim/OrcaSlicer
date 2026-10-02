# deps_src/libigl/igl/embree/EmbreeRenderer.h

- Hit · class · L41-L48 — struct Hit
- Dynamic · type · L52-L52 — typedef Eigen::Matrix<float,Eigen::Dynamic,3> ColorMatrixType;
- Dynamic · type · L53-L53 — typedef Eigen::Matrix<int,  Eigen::Dynamic,3> FaceMatrixType;
- Dynamic · type · L54-L54 — typedef Eigen::Matrix<unsigned char,Eigen::Dynamic,Eigen::Dynamic> PixelMatrixType;
- EmbreeRenderer · function · L63-L63 — virtual ~EmbreeRenderer();
- set_face_based · function · L124-L124 — void set_face_based(bool f);
- set_orthographic · function · L129-L129 — void set_orthographic(bool f );
- set_double_sided · function · L135-L135 — void set_double_sided(bool f);
- render_buffer · function · L145-L148 — void render_buffer(PixelMatrixType &R,
- intersect_ray · function · L161-L165 — bool intersect_ray(
- init · function · L179-L182 — void init(
- init · function · L193-L197 — void init(
- deinit · function · L203-L203 — void deinit();
- init_view · function · L205-L205 — void init_view();
- create_ray · function · L247-L253 — void create_ray(
