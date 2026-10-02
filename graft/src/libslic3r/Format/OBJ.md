# src/libslic3r/Format/OBJ.hpp

- TriangleMesh · class · L8-L8 — class TriangleMesh;
- Model · class · L9-L9 — class Model;
- ModelObject · class · L10-L10 — class ModelObject;
- ObjInfo · class · L12-L24 — struct ObjInfo
- ObjDialogInOut · class · L25-L35 — struct ObjDialogInOut
- ObjImportColorFn · type · L36-L36 — typedef std::function<void(ObjDialogInOut &in_out)> ObjImportColorFn;
- load_obj · function · L37-L37 — extern bool load_obj(const char *path, TriangleMesh *mesh, ObjInfo &vertex_colors, std::string &message, ObjParser::MtlData *out_mtl = nullptr);
- load_obj · function · L38-L38 — extern bool load_obj(const char *path, Model *model, ObjInfo &vertex_colors, std::string &message, const char *object_name = nullptr, ObjParser::MtlData *out_mtl = nullptr);
- obj_to_textured_mesh · function · L43-L48 — extern bool obj_to_textured_mesh(
- store_obj · function · L50-L50 — extern bool store_obj(const char *path, TriangleMesh *mesh);
- store_obj · function · L51-L51 — extern bool store_obj(const char *path, ModelObject *model);
- store_obj · function · L52-L52 — extern bool store_obj(const char *path, Model *model);
