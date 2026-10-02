# src/libslic3r/Support/SupportParameters.hpp

- number_of_support_interface_bottom_layers · function · L10-L15 — inline int number_of_support_interface_bottom_layers(const PrintObjectConfig& object_config)
- SupportParameters · class · L17-L326 — struct SupportParameters
- SupportParameters · function · L18-L18 — SupportParameters() = delete;
- SupportParameters · function · L19-L212 — SupportParameters(const PrintObject& object)
- has_contacts · function · L230-L230 — bool                    has_contacts() const { return this->has_top_contacts || this->has_bottom_contacts; }
- has_interfaces · function · L231-L231 — bool                    has_interfaces() const { return this->num_top_interface_layers + this->num_bottom_interface_layers > 0; }
- has_base_interfaces · function · L232-L232 — bool                    has_base_interfaces() const { return this->num_top_base_interface_layers + this->num_bottom_base_interface_layers > 0; }
- num_top_interface_layers_only · function · L233-L233 — size_t                  num_top_interface_layers_only() const { return this->num_top_interface_layers - this->num_top_base_interface_layers; }
- num_bottom_interface_layers_only · function · L234-L234 — size_t                  num_bottom_interface_layers_only() const { return this->num_bottom_interface_layers - this->num_bottom_base_interface_layers; }
- raft_interface_angle · function · L292-L293 — float 					raft_interface_angle(size_t interface_id) const
- support_interface_angle · function · L297-L317 — float 					support_interface_angle(size_t interface_id) const
