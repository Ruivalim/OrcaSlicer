# src/libslic3r/Arachne/BeadingStrategy/OuterWallInsetBeadingStrategy.hpp

- OuterWallInsetBeadingStrategy · class · L17-L36 — class OuterWallInsetBeadingStrategy : public BeadingStrategy
- OuterWallInsetBeadingStrategy · function · L20-L20 — OuterWallInsetBeadingStrategy(coord_t outer_wall_offset, BeadingStrategyPtr parent);
- compute · function · L24-L24 — Beading compute(coord_t thickness, coord_t bead_count) const override;
- getOptimalThickness · function · L26-L26 — coord_t getOptimalThickness(coord_t bead_count) const override;
- getTransitionThickness · function · L27-L27 — coord_t getTransitionThickness(coord_t lower_bead_count) const override;
- getOptimalBeadCount · function · L28-L28 — coord_t getOptimalBeadCount(coord_t thickness) const override;
- getTransitioningLength · function · L29-L29 — coord_t getTransitioningLength(coord_t lower_bead_count) const override;
- toString · function · L31-L31 — std::string toString() const override;
