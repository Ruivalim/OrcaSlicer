# src/slic3r/GUI/MarkdownTip.hpp

- MarkdownTip · class · L11-L62 — class MarkdownTip : public wxPopupTransientWindow
- ShowTip · function · L14-L14 — static bool ShowTip(std::string const &tip, std::string const &tooltip, wxPoint pos);
- ExitTip · function · L16-L16 — static void ExitTip();
- Reload · function · L18-L18 — static void Reload();
- Recreate · function · L20-L20 — static void Recreate(wxWindow *parent);
- AttachTo · function · L22-L22 — static wxWindow* AttachTo(wxWindow * parent);
- DetachFrom · function · L24-L24 — static wxWindow* DetachFrom(wxWindow * parent);
- markdownTip · function · L27-L27 — static MarkdownTip* markdownTip(bool create = true);
- MarkdownTip · function · L29-L29 — MarkdownTip();
- LoadStyle · function · L33-L33 — void LoadStyle();
- ShowTip · function · L35-L35 — bool ShowTip(wxPoint pos, std::string const &tip, std::string const & tooltip);
- LoadTip · function · L37-L37 — std::string LoadTip(std::string const &tip, std::string const &tooltip);
- RunScript · function · L39-L39 — void RunScript(std::string const& script);
- CreateTipView · function · L42-L42 — wxWebView* CreateTipView(wxWindow* parent);
- OnLoaded · function · L44-L44 — void OnLoaded(wxWebViewEvent& event);
- OnTitleChanged · function · L46-L46 — void OnTitleChanged(wxWebViewEvent& event);
- OnError · function · L48-L48 — void OnError(wxWebViewEvent& event);
- OnTimer · function · L50-L50 — void OnTimer(wxTimerEvent& event);
