# src/slic3r/GUI/PrinterCloudAuthDialog.hpp

- PrinterCloudAuthDialog · class · L24-L46 — class PrinterCloudAuthDialog : public wxDialog
- PrinterCloudAuthDialog · function · L35-L35 — PrinterCloudAuthDialog(wxWindow* parent, PrintHost* host);
- GetApiKey · function · L38-L38 — std::string GetApiKey() { return m_apikey; };
- OnNavigationRequest · function · L40-L40 — void OnNavigationRequest(wxWebViewEvent& evt);
- OnNavigationComplete · function · L41-L41 — void OnNavigationComplete(wxWebViewEvent& evt);
- OnDocumentLoaded · function · L42-L42 — void OnDocumentLoaded(wxWebViewEvent& evt);
- OnNewWindow · function · L43-L43 — void OnNewWindow(wxWebViewEvent& evt);
- OnScriptMessage · function · L44-L44 — void OnScriptMessage(wxWebViewEvent& evt);
