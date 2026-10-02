# src/slic3r/GUI/Jobs/SLAImportJob.hpp

- SLAImportJobView · class · L9-L19 — class SLAImportJobView
- Sel · type · L12-L12 — enum Sel { modelAndProfile, profileOnly, modelOnly };
- get_selection · function · L16-L16 — virtual Sel         get_selection() const          = 0;
- get_marchsq_windowsize · function · L17-L17 — virtual Vec2i32       get_marchsq_windowsize() const = 0;
- get_path · function · L18-L18 — virtual std::string get_path() const               = 0;
- Plater · class · L21-L21 — class Plater;
- SLAImportJob · class · L23-L38 — class SLAImportJob : public Job
- priv · class · L24-L24 — class priv;
- prepare · function · L30-L30 — void prepare();
- process · function · L31-L31 — void process(Ctl &ctl) override;
- finalize · function · L32-L32 — void finalize(bool canceled, std::exception_ptr &) override;
- SLAImportJob · function · L34-L34 — SLAImportJob(const SLAImportJobView *);
- reset · function · L37-L37 — void reset();
