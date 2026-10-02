# src/slic3r/GUI/Jobs/RotoptimizeJob.hpp

- Plater · class · L14-L14 — class Plater;
- RotoptimizeJob · class · L16-L72 — class RotoptimizeJob : public Job
- FindMethod · class · L21-L21 — struct FindMethod { std::string name; FindFn findfn; std::string descr; };
- ObjRot · class · L42-L47 — struct ObjRot
- ObjRot · function · L46-L46 — ObjRot(size_t id): idx{id}, rot{} {}
- prepare · function · L54-L54 — void prepare();
- process · function · L55-L55 — void process(Ctl &ctl) override;
- RotoptimizeJob · function · L57-L57 — RotoptimizeJob();
- finalize · function · L59-L59 — void finalize(bool canceled, std::exception_ptr &) override;
- get_methods_count · function · L61-L61 — static constexpr size_t get_methods_count() { return std::size(Methods); }
- get_method_name · function · L63-L66 — static std::string get_method_name(size_t i)
- get_method_description · function · L68-L71 — static std::string get_method_description(size_t i)
