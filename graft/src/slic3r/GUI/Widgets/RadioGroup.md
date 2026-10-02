# src/slic3r/GUI/Widgets/RadioGroup.hpp

- RadioGroup · class · L15-L72 — class RadioGroup : public wxPanel
- RadioGroup · function · L19-L19 — RadioGroup();
- RadioGroup · function · L21-L26 — RadioGroup(
- Create · function · L28-L33 — void Create(
- GetSelection · function · L35-L35 — int  GetSelection();
- SetSelection · function · L37-L37 — void SetSelection(int index, bool focus = false);
- SelectNext · function · L39-L39 — void SelectNext(bool focus = true);
- SelectPrevious · function · L41-L41 — void SelectPrevious(bool focus = true);
- Enable · function · L43-L43 — bool Enable(bool enable = true) override;
- IsEnabled · function · L45-L45 — bool IsEnabled();
- Disable · function · L47-L47 — bool Disable();
- SetRadioTooltip · function · L49-L49 — void SetRadioTooltip(int i, wxString tooltip);
- SetRadioIcon · function · L70-L70 — void SetRadioIcon(int i, bool hover);
