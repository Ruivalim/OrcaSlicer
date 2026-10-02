# src/libslic3r/SLA/Rotfinder.hpp

- ModelObject · class · L11-L11 — class ModelObject;
- SLAPrintObject · class · L12-L12 — class SLAPrintObject;
- TriangleMesh · class · L13-L13 — class TriangleMesh;
- DynamicPrintConfig · class · L14-L14 — class DynamicPrintConfig;
- RotOptimizeParams · class · L20-L42 — class RotOptimizeParams
- accuracy · function · L27-L27 — RotOptimizeParams &accuracy(float a) { m_accuracy = a; return *this; }
- print_config · function · L28-L28 — RotOptimizeParams &print_config(const DynamicPrintConfig *c)
- statucb · function · L33-L33 — RotOptimizeParams &statucb(RotOptimizeStatusCB cb)
- accuracy · function · L39-L39 — float accuracy() const { return m_accuracy; }
- print_config · function · L40-L40 — const DynamicPrintConfig * print_config() const { return m_print_config; }
- statuscb · function · L41-L41 — const RotOptimizeStatusCB &statuscb() const { return m_statuscb; }
- find_best_misalignment_rotation · function · L60-L61 — Vec2d find_best_misalignment_rotation(const ModelObject &modelobj,
- find_least_supports_rotation · function · L63-L64 — Vec2d find_least_supports_rotation(const ModelObject &modelobj,
- find_min_z_height_rotation · function · L66-L67 — Vec2d find_min_z_height_rotation(const ModelObject &mo,
