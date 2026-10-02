# src/libslic3r/PerimeterGenerator.hpp

- FuzzySkinConfig · class · L13-L46 — struct FuzzySkinConfig
- PerimeterGenerator · class · L73-L171 — class PerimeterGenerator
- PerimeterGenerator · function · L109-L139 — PerimeterGenerator(
- process_classic · function · L141-L141 — void        process_classic();
- process_arachne · function · L142-L142 — void        process_arachne();
- add_infill_contour_for_arachne · function · L144-L144 — void        add_infill_contour_for_arachne( ExPolygons infill_contour, int loops, coord_t ext_perimeter_spacing, coord_t perimeter_spacing, coord_t min_perimeter_infill_spacing, coord_t spacing, bool is_inner_part );
- ext_mm3_per_mm · function · L146-L146 — double      ext_mm3_per_mm()        const { return m_ext_mm3_per_mm; }
- mm3_per_mm · function · L147-L147 — double      mm3_per_mm()            const { return m_mm3_per_mm; }
- mm3_per_mm_overhang · function · L148-L148 — double      mm3_per_mm_overhang()   const { return m_mm3_per_mm_overhang; }
- smaller_width_ext_mm3_per_mm · function · L150-L150 — double      smaller_width_ext_mm3_per_mm()   const { return m_ext_mm3_per_mm_smaller_width; }
- lower_slices_polygons · function · L151-L151 — Polygons    lower_slices_polygons() const { return m_lower_slices_polygons; }
- printable_slices · function · L153-L153 — ExPolygons  printable_slices(const ExPolygons &slices) const;
- generate_lower_polygons_series · function · L156-L156 — std::vector<Polygons>     generate_lower_polygons_series(float width);
- split_top_surfaces · function · L157-L157 — void split_top_surfaces(const ExPolygons &orig_polygons, ExPolygons &top_fills, ExPolygons &non_top_polygons, ExPolygons &fill_clip) const;
- apply_extra_perimeters · function · L158-L158 — void apply_extra_perimeters(ExPolygons& infill_area);
- process_no_bridge · function · L159-L159 — void process_no_bridge(Surfaces& all_surfaces, coord_t perimeter_spacing, coord_t ext_perimeter_width);
