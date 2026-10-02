# src/libslic3r/ModelArrange.hpp

- throw_if_out_of_bed · function · L20-L23 — [[noreturn]] inline void throw_if_out_of_bed(arrangement::ArrangePolygon& ap)
- get_arrange_polys · function · L25-L25 — ArrangePolygons get_arrange_polys(const Model &model, ModelInstancePtrs &instances);
- get_arrange_poly · function · L26-L26 — ArrangePolygon  get_arrange_poly(const Model &model);
- apply_arrange_polys · function · L27-L27 — bool apply_arrange_polys(ArrangePolygons &polys, ModelInstancePtrs &instances, VirtualBedFn);
- duplicate · function · L29-L29 — void duplicate(Model &model, ArrangePolygons &copies, VirtualBedFn);
- duplicate_objects · function · L30-L30 — void duplicate_objects(Model &model, size_t copies_num);
- arrange_objects · function · L32-L43 — template<class TBed>
- duplicate · function · L45-L55 — template<class TBed>
- copies · function · L52-L52 — ArrangePolygons copies(copies_num, get_arrange_poly(model));
- duplicate_objects · function · L57-L66 — template<class TBed>
- PtrWrapper · class · L68-L86 — template<class T> struct PtrWrapper
- PtrWrapper · function · L72-L72 — explicit PtrWrapper(T* p) : ptr{ p } {}
- get_arrange_polygon · function · L74-L79 — arrangement::ArrangePolygon get_arrange_polygon(const Slic3r::DynamicPrintConfig &config = Slic3r::DynamicPrintConfig()) const
- apply_arrange_result · function · L81-L85 — void apply_arrange_result(const Vec2d& t, double rot, int item_id)
- get_arrange_poly · function · L88-L89 — template<class T>
- get_arrange_poly · function · L91-L92 — template<>
- get_instance_arrange_poly · function · L94-L94 — ArrangePolygon get_instance_arrange_poly(ModelInstance* instance, const DynamicPrintConfig& config);
