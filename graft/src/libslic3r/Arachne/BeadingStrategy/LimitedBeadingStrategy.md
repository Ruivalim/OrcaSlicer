# src/libslic3r/Arachne/BeadingStrategy/LimitedBeadingStrategy.hpp

- LimitedBeadingStrategy · class · L29-L49 — class LimitedBeadingStrategy : public BeadingStrategy
- LimitedBeadingStrategy · function · L32-L32 — LimitedBeadingStrategy(coord_t max_bead_count, BeadingStrategyPtr parent);
- compute · function · L36-L36 — Beading compute(coord_t thickness, coord_t bead_count) const override;
- getOptimalThickness · function · L37-L37 — coord_t getOptimalThickness(coord_t bead_count) const override;
- getTransitionThickness · function · L38-L38 — coord_t getTransitionThickness(coord_t lower_bead_count) const override;
- getOptimalBeadCount · function · L39-L39 — coord_t getOptimalBeadCount(coord_t thickness) const override;
- toString · function · L40-L40 — std::string toString() const override;
- getTransitioningLength · function · L42-L42 — coord_t getTransitioningLength(coord_t lower_bead_count) const override;
- getTransitionAnchorPos · function · L44-L44 — float getTransitionAnchorPos(coord_t lower_bead_count) const override;
