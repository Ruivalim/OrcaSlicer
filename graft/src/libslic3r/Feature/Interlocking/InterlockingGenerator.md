# src/libslic3r/Feature/Interlocking/InterlockingGenerator.hpp

- InterlockingGenerator · class · L42-L172 — class InterlockingGenerator
- generate_interlocking_structure · function · L48-L48 — static void generate_interlocking_structure(PrintObject* print_object, const std::function<void()>& throw_on_cancel);
- generateInterlockingStructure · function · L54-L54 — void generateInterlockingStructure() const;
- InterlockingGenerator · function · L68-L93 — InterlockingGenerator(PrintObject&          print_object,
- growBorderAreasPerpendicular · function · L102-L102 — std::pair<ExPolygons, ExPolygons> growBorderAreasPerpendicular(const ExPolygons& a, const ExPolygons& b, const coord_t& detect) const;
- handleThinAreas · function · L109-L109 — void handleThinAreas(const std::unordered_set<GridPoint3>& has_all_meshes) const;
- getShellVoxels · function · L118-L118 — std::vector<std::unordered_set<GridPoint3>> getShellVoxels(const DilationKernel& kernel) const;
- addBoundaryCells · function · L128-L128 — void addBoundaryCells(const std::vector<ExPolygons>& layers, const DilationKernel& kernel, std::unordered_set<GridPoint3>& cells) const;
- computeUnionedVolumeRegions · function · L136-L136 — std::vector<ExPolygons> computeUnionedVolumeRegions() const;
- generateMicrostructure · function · L142-L142 — std::vector<std::vector<ExPolygons>> generateMicrostructure() const;
- applyMicrostructureToOutlines · function · L150-L150 — void applyMicrostructureToOutlines(const std::unordered_set<GridPoint3>& cells, const std::vector<ExPolygons>& layer_regions) const;
