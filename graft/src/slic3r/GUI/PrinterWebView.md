# src/slic3r/GUI/PrinterWebView.hpp

- PrinterWebViewHandler · class · L34-L34 — class PrinterWebViewHandler;
- PrinterWebView · class · L37-L67 — class PrinterWebView : public wxPanel
- PrinterWebView · function · L39-L39 — PrinterWebView(wxWindow *parent);
- load_url · function · L42-L42 — void load_url(wxString& url, wxString apikey = "");
- UpdateState · function · L43-L43 — void UpdateState();
- OnClose · function · L44-L44 — void OnClose(wxCloseEvent& evt);
- OnError · function · L45-L45 — void OnError(wxWebViewEvent& evt);
- OnLoaded · function · L46-L46 — void OnLoaded(wxWebViewEvent& evt);
- OnNewWindow · function · L47-L47 — void OnNewWindow(wxWebViewEvent& evt);
- OnScriptMessage · function · L48-L48 — void OnScriptMessage(wxWebViewEvent& evt);
- reload · function · L49-L49 — void reload();
- update_mode · function · L50-L50 — void update_mode();
- Show · function · L52-L52 — bool Show(bool show = true) override;
- SendAPIKey · function · L57-L57 — void SendAPIKey();
