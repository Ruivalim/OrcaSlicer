# src/libslic3r/PrintRegion.cpp

- extruder · method · L7-L23 — unsigned int PrintRegion::extruder(FlowRole role) const
- flow · method · L25-L54 — Flow PrintRegion::flow(const PrintObject &object, FlowRole role, double layer_height, bool first_layer) const
- nozzle_dmr_avg · method · L56-L64 — coordf_t PrintRegion::nozzle_dmr_avg(const PrintConfig &print_config) const
- bridging_height_avg · method · L66-L69 — coordf_t PrintRegion::bridging_height_avg(const PrintConfig &print_config) const
- collect_object_printing_extruders · method · L71-L93 — void PrintRegion::collect_object_printing_extruders(const PrintConfig &print_config, const PrintRegionConfig &region_config, const bool has_brim, std::vector<unsigned int> &object_extruders)
- collect_object_printing_extruders · method · L95-L110 — void PrintRegion::collect_object_printing_extruders(const Print &print, std::vector<unsigned int> &object_extruders) const
