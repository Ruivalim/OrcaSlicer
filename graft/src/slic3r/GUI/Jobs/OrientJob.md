# src/slic3r/GUI/Jobs/OrientJob.hpp

- ModelObject · class · L9-L9 — class ModelObject;
- Plater · class · L13-L13 — class Plater;
- OrientJob · class · L15-L60 — class OrientJob : public Job
- clear_input · function · L24-L24 — void clear_input();
- prepare_selection · function · L27-L27 — void prepare_selection(std::vector<bool> obj_sel, bool only_one_plate);
- prepare_selected · function · L31-L31 — void prepare_selected();
- prepare_partplate · function · L34-L34 — void prepare_partplate();
- prepare · function · L37-L37 — void prepare();
- process · function · L39-L39 — void process(Ctl &ctl) override;
- OrientJob · function · L41-L41 — OrientJob();
- finalize · function · L43-L43 — void finalize(bool canceled, std::exception_ptr &e) override;
- get_orient_mesh · function · L45-L57 — static
- get_orient_mesh · function · L59-L59 — static orientation::OrientMesh get_orient_mesh(ModelInstance* instance);
