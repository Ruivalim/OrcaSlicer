# src/libslic3r/CAD/ThreadStandards.hpp

- ThreadSpec · class · L15-L29 — struct ThreadSpec
- Series · type · L16-L16 — enum class Series { MetricCoarse, MetricFine, UNC, UNF };
- thread_depth_mm · function · L24-L24 — double thread_depth_mm() const { return 0.6134 * pitch_mm; }
- minor_diameter_mm · function · L26-L26 — double minor_diameter_mm() const { return major_diameter_mm - 1.0825 * pitch_mm; }
- imperial · function · L28-L28 — bool imperial() const { return series == Series::UNC || series == Series::UNF; }
- thread_standards · function · L32-L32 — const std::vector<ThreadSpec>& thread_standards();
- find_thread_standard · function · L35-L35 — const ThreadSpec* find_thread_standard(const std::string& name);
