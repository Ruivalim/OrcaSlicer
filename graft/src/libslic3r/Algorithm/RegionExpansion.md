# src/libslic3r/Algorithm/RegionExpansion.hpp

- RegionExpansionParameters · class · L12-L37 — struct RegionExpansionParameters
- build · function · L30-L36 — static RegionExpansionParameters build(
- WaveSeed · class · L39-L43 — struct WaveSeed
- lower_by_boundary_and_src · function · L46-L49 — inline bool lower_by_boundary_and_src(const WaveSeed &l, const WaveSeed &r)
- lower_by_src_and_boundary · function · L51-L54 — inline bool lower_by_src_and_boundary(const WaveSeed &l, const WaveSeed &r)
- wave_seeds · function · L58-L65 — WaveSeeds wave_seeds(
- RegionExpansion · class · L67-L72 — struct RegionExpansion
- propagate_waves · function · L74-L74 — std::vector<RegionExpansion> propagate_waves(const WaveSeeds &seeds, const ExPolygons &boundary, const RegionExpansionParameters &params);
- propagate_waves · function · L75-L75 — std::vector<RegionExpansion> propagate_waves(const ExPolygons &src, const ExPolygons &boundary, const RegionExpansionParameters &params);
- propagate_waves · function · L77-L83 — std::vector<RegionExpansion> propagate_waves(const ExPolygons &src, const ExPolygons &boundary,
- RegionExpansionEx · class · L85-L90 — struct RegionExpansionEx
- propagate_waves_ex · function · L92-L92 — std::vector<RegionExpansionEx> propagate_waves_ex(const WaveSeeds &seeds, const ExPolygons &boundary, const RegionExpansionParameters &params);
- propagate_waves_ex · function · L94-L100 — std::vector<RegionExpansionEx> propagate_waves_ex(const ExPolygons &src, const ExPolygons &boundary,
- expand_expolygons · function · L102-L108 — std::vector<Polygons> expand_expolygons(const ExPolygons &src, const ExPolygons &boundary,
- merge_expansions_into_expolygons · function · L111-L111 — std::vector<ExPolygon> merge_expansions_into_expolygons(ExPolygons &&src, std::vector<RegionExpansion> &&expanded);
- expand_merge_expolygons · function · L113-L113 — std::vector<ExPolygon> expand_merge_expolygons(ExPolygons &&src, const ExPolygons &boundary, const RegionExpansionParameters &params);
