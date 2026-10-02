# src/libslic3r/Format/DRC.hpp

- TriangleMesh · class · L12-L12 — class TriangleMesh;
- ModelObject · class · L13-L13 — class ModelObject;
- Model · class · L14-L14 — class Model;
- load_drc · function · L17-L17 — extern bool load_drc(const char *path, TriangleMesh *meshptr);
- load_drc · function · L18-L18 — extern bool load_drc(const char *path, Model *model, const char *object_name = nullptr);
- store_drc · function · L20-L20 — extern bool store_drc(const char* path, TriangleMesh* mesh, int bits, int speed = DRC_SPEED_DEFAULT);
- store_drc · function · L21-L21 — extern bool store_drc(const char* path, ModelObject* model_object, int bits, int speed = DRC_SPEED_DEFAULT);
- store_drc · function · L22-L22 — extern bool store_drc(const char* path, Model* model, int bits, int speed = DRC_SPEED_DEFAULT);
