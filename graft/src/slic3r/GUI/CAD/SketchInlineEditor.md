# src/slic3r/GUI/CAD/SketchInlineEditor.hpp

- ImGuiWrapper · class · L12-L12 — class ImGuiWrapper;
- SketchInlineEditor · class · L37-L91 — class SketchInlineEditor
- SketchInlineEditor · function · L40-L40 — SketchInlineEditor() = default;
- open · function · L45-L47 — void open(const wxPoint& canvas_px, double value, const std::string& title,
- close · function · L48-L48 — void close();                        // drop it with neither callback
- cancel · function · L49-L49 — void cancel();                       // if open, run the registered cancel (keep-as-drawn)
- commit · function · L50-L50 — void commit();                       // if open, run the registered commit (accept the typed value)
- is_open · function · L51-L51 — bool is_open() const { return m_open; }
- render · function · L55-L55 — bool render(ImGuiWrapper& imgui, float scale);
- is_mapped · function · L75-L75 — bool is_mapped() const { return m_open; }
- has_focus · function · L76-L76 — bool has_focus() const { return m_open; }
- dismiss · function · L77-L77 — void dismiss() { close(); }
- do_commit · function · L80-L80 — void do_commit();
- do_cancel · function · L81-L81 — void do_cancel();
