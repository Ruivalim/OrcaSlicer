# src/libslic3r/Format/SL1.hpp

- SL1Archive · class · L11-L39 — class SL1Archive: public SLAArchive
- create_raster · function · L15-L15 — std::unique_ptr<sla::RasterBase> create_raster() const override;
- get_encoder · function · L16-L16 — sla::RasterEncoder get_encoder() const override;
- SL1Archive · function · L20-L20 — SL1Archive() = default;
- SL1Archive · function · L21-L21 — explicit SL1Archive(const SLAPrinterConfig &cfg): m_cfg(cfg) {}
- SL1Archive · function · L22-L22 — explicit SL1Archive(SLAPrinterConfig &&cfg): m_cfg(std::move(cfg)) {}
- export_print · function · L24-L24 — void export_print(Zipper &zipper, const SLAPrint &print, const std::string &projectname = "");
- export_print · function · L25-L29 — void export_print(const std::string &fname, const SLAPrint &print, const std::string &projectname = "")
- zipper · function · L27-L27 — Zipper zipper(fname);
- apply · function · L31-L38 — void apply(const SLAPrinterConfig &cfg) override
- import_sla_archive · function · L41-L41 — ConfigSubstitutions import_sla_archive(const std::string &zipfname, DynamicPrintConfig &out);
- import_sla_archive · function · L43-L48 — ConfigSubstitutions import_sla_archive(
- import_sla_archive · function · L50-L58 — inline ConfigSubstitutions import_sla_archive(
- MissingProfileError · class · L60-L60 — class MissingProfileError : public RuntimeError { using RuntimeError::RuntimeError; };
