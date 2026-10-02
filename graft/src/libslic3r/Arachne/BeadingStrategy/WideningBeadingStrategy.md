# src/libslic3r/Arachne/BeadingStrategy/WideningBeadingStrategy.hpp

- WideningBeadingStrategy · class · L24-L47 — class WideningBeadingStrategy : public BeadingStrategy
- WideningBeadingStrategy · function · L30-L30 — WideningBeadingStrategy(BeadingStrategyPtr parent, coord_t min_input_width, coord_t min_output_width);
- compute · function · L34-L34 — Beading compute(coord_t thickness, coord_t bead_count) const override;
- getOptimalThickness · function · L35-L35 — coord_t getOptimalThickness(coord_t bead_count) const override;
- getTransitionThickness · function · L36-L36 — coord_t getTransitionThickness(coord_t lower_bead_count) const override;
- getOptimalBeadCount · function · L37-L37 — coord_t getOptimalBeadCount(coord_t thickness) const override;
- getTransitioningLength · function · L38-L38 — coord_t getTransitioningLength(coord_t lower_bead_count) const override;
- getTransitionAnchorPos · function · L39-L39 — float getTransitionAnchorPos(coord_t lower_bead_count) const override;
- getNonlinearThicknesses · function · L40-L40 — std::vector<coord_t> getNonlinearThicknesses(coord_t lower_bead_count) const override;
- toString · function · L41-L41 — std::string toString() const override;
