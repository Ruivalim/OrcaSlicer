# src/libslic3r/Support/SupportMaterial.hpp

- PrintObject · class · L12-L12 — class PrintObject;
- PrintConfig · class · L13-L13 — class PrintConfig;
- PrintObjectConfig · class · L14-L14 — class PrintObjectConfig;
- PrintObjectSupportMaterial · class · L20-L96 — class PrintObjectSupportMaterial
- PrintObjectSupportMaterial · function · L23-L23 — PrintObjectSupportMaterial(const PrintObject *object, const SlicingParameters &slicing_params);
- has_raft · function · L26-L26 — bool 		has_raft() 					const { return m_slicing_params.has_raft(); }
- has_support · function · L28-L28 — bool 		has_support()				const { return m_object_config->enable_support.value || m_object_config->enforce_support_layers; }
- build_plate_only · function · L29-L29 — bool 		build_plate_only() 			const { return this->has_support() && m_object_config->support_on_build_plate_only.value; }
- synchronize_layers · function · L31-L31 — bool 		synchronize_layers()		const { return /*m_slicing_params.zero_gap_interface_top && */!m_print_config->independent_support_layer_height.value; }
- has_contact_loops · function · L32-L32 — bool 		has_contact_loops() 		const { return m_object_config->support_interface_loop_pattern.value; }
- generate · function · L37-L37 — void 		generate(PrintObject &object);
- buildplate_covered · function · L40-L40 — std::vector<Polygons> buildplate_covered(const PrintObject &object) const;
- top_contact_layers · function · L45-L45 — SupportGeneratorLayersPtr top_contact_layers(const PrintObject &object, const std::vector<Polygons> &buildplate_covered, SupportGeneratorLayerStorage &layer_storage) const;
- bottom_contact_layers_and_layer_support_areas · function · L50-L52 — SupportGeneratorLayersPtr bottom_contact_layers_and_layer_support_areas(
- trim_top_contacts_by_bottom_contacts · function · L55-L55 — void trim_top_contacts_by_bottom_contacts(const PrintObject &object, const SupportGeneratorLayersPtr &bottom_contacts, SupportGeneratorLayersPtr &top_contacts) const;
- raft_and_intermediate_support_layers · function · L58-L62 — SupportGeneratorLayersPtr raft_and_intermediate_support_layers(
- generate_base_layers · function · L65-L70 — void generate_base_layers(
- trim_support_layers_by_object · function · L76-L81 — void trim_support_layers_by_object(
