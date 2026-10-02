# src/libslic3r/Format/STL.hpp

- Model · class · L8-L8 — class Model;
- TriangleMesh · class · L9-L9 — class TriangleMesh;
- ModelObject · class · L10-L10 — class ModelObject;
- load_stl · function · L13-L13 — extern bool load_stl(const char *path, Model *model, const char *object_name = nullptr, ImportstlProgressFn stlFn = nullptr, int custom_header_length = 80);
- store_stl · function · L15-L15 — extern bool store_stl(const char *path, TriangleMesh *mesh, bool binary);
- store_stl · function · L16-L16 — extern bool store_stl(const char *path, ModelObject *model_object, bool binary);
- store_stl · function · L17-L17 — extern bool store_stl(const char *path, Model *model, bool binary);
