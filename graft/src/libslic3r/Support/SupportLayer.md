# src/libslic3r/Support/SupportLayer.hpp

- SupporLayerType · type · L15-L35 — enum class SupporLayerType
- SupportGeneratorLayer · class · L40-L113 — class SupportGeneratorLayer
- reset · function · L43-L45 — void reset()
- merge · function · L67-L80 — void merge(SupportGeneratorLayer &&rhs)
- bottom_print_z · function · L84-L84 — coordf_t bottom_print_z() const { return print_z - height; }
- extreme_z · function · L87-L87 — coordf_t extreme_z() const { return (this->layer_type == SupporLayerType::TopContact) ? this->bottom_z : this->print_z; }
- SupportGeneratorLayerStorage · class · L118-L141 — class SupportGeneratorLayerStorage
- allocate_unguarded · function · L120-L120 — SupportGeneratorLayer& allocate_unguarded(SupporLayerType layer_type)
- allocate · function · L126-L126 — SupportGeneratorLayer& allocate(SupporLayerType layer_type)
