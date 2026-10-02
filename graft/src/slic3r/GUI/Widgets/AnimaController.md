# src/slic3r/GUI/Widgets/AnimaController.hpp

- AnimaIcon · class · L8-L28 — class AnimaIcon : public wxPanel
- AnimaIcon · function · L11-L11 — AnimaIcon(wxWindow *parent, wxWindowID id, std::vector<std::string> img_list, std::string img_enable, int ivt = 1000);
- Play · function · L14-L14 — void Play();
- Stop · function · L15-L15 — void Stop();
- ShowEnabledIcon · function · L16-L16 — void ShowEnabledIcon();
- IsPlaying · function · L17-L17 — bool IsPlaying() const { return IsRunning(); };
- IsRunning · function · L18-L18 — bool IsRunning() const;
