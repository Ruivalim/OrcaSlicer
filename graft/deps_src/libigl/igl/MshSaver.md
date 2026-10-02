# deps_src/libigl/igl/MshSaver.h

- IndexVector · type · L26-L26 — typedef std::vector<int>         IndexVector;
- IntVector · type · L27-L27 — typedef std::vector<int>         IntVector;
- FloatVector · type · L28-L28 — typedef std::vector<Float>       FloatVector;
- FloatField · type · L29-L29 — typedef std::vector<FloatVector> FloatField;
- IntField · type · L30-L30 — typedef std::vector<IntVector>   IntField;
- FieldNames · type · L31-L31 — typedef std::vector<std::string> FieldNames;
- save_mesh · function · L46-L51 — void save_mesh(
- save_scalar_field · function · L56-L56 — void save_scalar_field(const std::string& fieldname, const FloatVector& field);
- save_vector_field · function · L58-L58 — void save_vector_field(const std::string& fieldname, const FloatVector& field);
- save_elem_scalar_field · function · L60-L60 — void save_elem_scalar_field(const std::string& fieldname, const FloatVector& field);
- save_elem_vector_field · function · L62-L62 — void save_elem_vector_field(const std::string& fieldname, const FloatVector& field);
- save_elem_tensor_field · function · L64-L64 — void save_elem_tensor_field(const std::string& fieldname, const FloatVector& field);
- save_header · function · L67-L67 — void save_header();
- save_nodes · function · L68-L68 — void save_nodes(const FloatVector& nodes);
- save_elements · function · L69-L72 — void save_elements(const IndexVector& elements,
