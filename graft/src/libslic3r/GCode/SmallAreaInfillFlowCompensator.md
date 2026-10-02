# src/libslic3r/GCode/SmallAreaInfillFlowCompensator.hpp

- SmallAreaInfillFlowCompensator · class · L12-L31 — class SmallAreaInfillFlowCompensator
- SmallAreaInfillFlowCompensator · function · L15-L15 — SmallAreaInfillFlowCompensator() = delete;
- SmallAreaInfillFlowCompensator · function · L16-L16 — explicit SmallAreaInfillFlowCompensator(const Slic3r::GCodeConfig& config);
- modify_flow · function · L19-L19 — double modify_flow(const double line_length, const double dE, const ExtrusionRole role);
- flow_comp_model · function · L28-L28 — double flow_comp_model(const double line_length);
- max_modified_length · function · L30-L30 — double max_modified_length() { return eLengths.back(); }
