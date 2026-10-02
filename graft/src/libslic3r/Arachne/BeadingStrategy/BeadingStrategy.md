# src/libslic3r/Arachne/BeadingStrategy/BeadingStrategy.hpp

- pi_div · function · L18-L18 — template<typename T> constexpr T pi_div(const T div) { return static_cast<T>(M_PI) / div; }
- BeadingStrategy · class · L29-L116 — class BeadingStrategy
- Beading · class · L35-L41 — struct Beading
- BeadingStrategy · function · L43-L43 — BeadingStrategy(coord_t optimal_width, double wall_split_middle_threshold, double wall_add_middle_threshold, coord_t default_transition_length, float transitioning_angle = pi_div(3));
- BeadingStrategy · function · L45-L45 — BeadingStrategy(const BeadingStrategy &other);
- compute · function · L56-L56 — virtual Beading compute(coord_t thickness, coord_t bead_count) const = 0;
- getOptimalThickness · function · L61-L61 — virtual coord_t getOptimalThickness(coord_t bead_count) const;
- getTransitionThickness · function · L66-L66 — virtual coord_t getTransitionThickness(coord_t lower_bead_count) const;
- getOptimalBeadCount · function · L71-L71 — virtual coord_t getOptimalBeadCount(coord_t thickness) const = 0;
- getTransitioningLength · function · L78-L78 — virtual coord_t getTransitioningLength(coord_t lower_bead_count) const;
- getTransitionAnchorPos · function · L85-L85 — virtual float getTransitionAnchorPos(coord_t lower_bead_count) const;
- getNonlinearThicknesses · function · L93-L93 — virtual std::vector<coord_t> getNonlinearThicknesses(coord_t lower_bead_count) const;
- toString · function · L95-L95 — virtual std::string toString() const;
- getSplitMiddleThreshold · function · L97-L97 — double  getSplitMiddleThreshold() const;
- getTransitioningAngle · function · L98-L98 — double  getTransitioningAngle() const;
