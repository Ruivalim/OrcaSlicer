# src/libslic3r/Arachne/BeadingStrategy/RedistributeBeadingStrategy.hpp

- RedistributeBeadingStrategy · class · L29-L56 — class RedistributeBeadingStrategy : public BeadingStrategy
- RedistributeBeadingStrategy · function · L38-L38 — RedistributeBeadingStrategy(coord_t optimal_width_outer, double minimum_variable_line_ratio, BeadingStrategyPtr parent);
- compute · function · L42-L42 — Beading compute(coord_t thickness, coord_t bead_count) const override;
- getOptimalThickness · function · L44-L44 — coord_t getOptimalThickness(coord_t bead_count) const override;
- getTransitionThickness · function · L45-L45 — coord_t getTransitionThickness(coord_t lower_bead_count) const override;
- getOptimalBeadCount · function · L46-L46 — coord_t getOptimalBeadCount(coord_t thickness) const override;
- getTransitioningLength · function · L47-L47 — coord_t getTransitioningLength(coord_t lower_bead_count) const override;
- getTransitionAnchorPos · function · L48-L48 — float getTransitionAnchorPos(coord_t lower_bead_count) const override;
- toString · function · L50-L50 — std::string toString() const override;
