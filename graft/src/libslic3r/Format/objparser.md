# src/libslic3r/Format/objparser.hpp

- ObjVertex · class · L12-L17 — struct ObjVertex
- ObjUseMtl · class · L26-L33 — struct ObjUseMtl
- ObjNewMtl · class · L35-L49 — struct ObjNewMtl
- ObjObject · class · L57-L61 — struct ObjObject
- ObjGroup · class · L70-L74 — struct ObjGroup
- ObjSmoothingGroup · class · L82-L86 — struct ObjSmoothingGroup
- ObjData · class · L96-L118 — struct ObjData
- MtlData · class · L120-L128 — struct MtlData
- objparse · function · L129-L129 — extern bool objparse(const char *path, ObjData &data);
- mtlparse · function · L130-L130 — extern bool mtlparse(const char *path, MtlData &data);
- objparse · function · L131-L131 — extern bool objparse(std::istream &stream, ObjData &data);
- objbinsave · function · L133-L133 — extern bool objbinsave(const char *path, const ObjData &data);
- objbinload · function · L135-L135 — extern bool objbinload(const char *path, ObjData &data);
- objequal · function · L137-L137 — extern bool objequal(const ObjData &data1, const ObjData &data2);
