# src/libslic3r/GCode/AdaptivePAProcessor.hpp

- GCode · class · L20-L20 — class GCode;
- AdaptivePAProcessor · class · L25-L95 — class AdaptivePAProcessor
- AdaptivePAProcessor · function · L36-L36 — AdaptivePAProcessor(GCode &gcodegen, const std::vector<unsigned int> &tools_used);
- process_layer · function · L47-L47 — std::string process_layer(std::string &&gcode);
- resetPreviousPA · function · L55-L55 — void resetPreviousPA(double PA){ m_last_predicted_pa = PA; };
- validate_adaptive_pa_model · function · L69-L69 — static std::string validate_adaptive_pa_model(const std::string& model_str);
- getInterpolator · function · L94-L94 — AdaptivePAInterpolator* getInterpolator(unsigned int tool_id);
