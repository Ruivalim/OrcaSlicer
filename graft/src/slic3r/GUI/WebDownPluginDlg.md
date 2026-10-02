# src/slic3r/GUI/WebDownPluginDlg.hpp

- DownPluginFrame · class · L33-L80 — class DownPluginFrame : public wxDialog
- DownPluginFrame · function · L36-L36 — DownPluginFrame(GUI_App *pGUI);
- load_url · function · L41-L41 — void     load_url(wxString &url);
- UpdateState · function · L43-L43 — void UpdateState();
- OnIdle · function · L44-L44 — void OnIdle(wxIdleEvent &evt);
- OnNavigationRequest · function · L47-L47 — void OnNavigationRequest(wxWebViewEvent &evt);
- OnNavigationComplete · function · L48-L48 — void OnNavigationComplete(wxWebViewEvent &evt);
- OnDocumentLoaded · function · L49-L49 — void OnDocumentLoaded(wxWebViewEvent &evt);
- OnNewWindow · function · L50-L50 — void OnNewWindow(wxWebViewEvent &evt);
- OnError · function · L51-L51 — void OnError(wxWebViewEvent &evt);
- OnTitleChanged · function · L52-L52 — void OnTitleChanged(wxWebViewEvent &evt);
- OnFullScreenChanged · function · L53-L53 — void OnFullScreenChanged(wxWebViewEvent &evt);
- OnScriptMessage · function · L54-L54 — void OnScriptMessage(wxWebViewEvent &evt);
- OnScriptResponseMessage · function · L56-L56 — void OnScriptResponseMessage(wxCommandEvent &evt);
- RunScript · function · L57-L57 — void RunScript(const wxString &javascript);
- DownloadPlugin · function · L60-L60 — int DownloadPlugin();
- InstallPlugin · function · L61-L61 — int InstallPlugin();
- ShowPluginStatus · function · L62-L62 — int ShowPluginStatus(int status, int percent, bool &cancel);
