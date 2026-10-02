# src/OrcaSlicer.hpp

- ExportFormat · type · L12-L19 — enum ExportFormat : int
- _height_range_info · class · L43-L48 — typedef struct _height_range_info
- _assembled_param_info · class · L50-L53 — typedef struct _assembled_param_info
- _assemble_object_info · class · L55-L66 — typedef struct _assemble_object_info
- _assemble_plate_info · class · L68-L77 — typedef struct _assemble_plate_info
- _printer_plate_info · class · L80-L95 — typedef struct _printer_plate_info
- _plate_obj_size_info · class · L97-L104 — typedef struct _plate_obj_size_info
- CLI · class · L107-L142 — class CLI
- run · function · L109-L109 — int run(int argc, char **argv);
- setup · function · L122-L122 — bool setup(int argc, char **argv);
- print_help · function · L125-L125 — void print_help(bool include_print_options = false, PrinterTechnology printer_technology = ptAny) const;
- export_models · function · L128-L128 — bool export_models(IO::ExportFormat format, std::string path = std::string());
- export_project · function · L130-L136 — bool export_project(Model *model, std::string& path, PlateDataPtrs &partplate_data, std::vector<Preset*>& project_presets,
- has_print_action · function · L138-L138 — bool has_print_action() const { return m_config.opt_bool("export_gcode") || m_config.opt_bool("export_sla"); }
- output_filepath · function · L140-L140 — std::string output_filepath(const Model &model, IO::ExportFormat format) const;
- output_filepath · function · L141-L141 — std::string output_filepath(const ModelObject &object, unsigned int index, IO::ExportFormat format, std::string path_dir) const;
