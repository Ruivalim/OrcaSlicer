# src/slic3r/GUI/KeyChord.hpp

- wxKeyEvent · class · L11-L11 — class wxKeyEvent;
- KeyChord · class · L19-L57 — struct KeyChord
- valid · function · L24-L24 — bool valid() const { return key != WXK_NONE; }
- is_punctuation · function · L30-L30 — bool is_punctuation() const;
- needs_char_event · function · L33-L33 — bool needs_char_event() const;
- is_menu_accelerator · function · L36-L36 — bool is_menu_accelerator() const;
- to_string · function · L39-L39 — std::string to_string() const;
- parse · function · L40-L40 — static std::optional<KeyChord> parse(const std::string& text);
- display · function · L44-L44 — std::string display() const;
- display_parts · function · L46-L46 — std::vector<std::string> display_parts() const;
- modifier_prefix · function · L48-L48 — static std::string modifier_prefix(int modifier);
- modifier_name · function · L49-L49 — static std::string modifier_name(int modifier);
- to_accelerator_entry · function · L51-L51 — wxAcceleratorEntry to_accelerator_entry(int command) const;
- from_event · function · L56-L56 — static KeyChord from_event(const wxKeyEvent& evt);
- KeyChordHash · class · L59-L62 — struct KeyChordHash
