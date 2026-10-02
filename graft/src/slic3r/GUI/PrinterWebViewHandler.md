# src/slic3r/GUI/PrinterWebViewHandler.hpp

- wxWebView · class · L8-L8 — class wxWebView;
- PrinterWebView · class · L13-L13 — class PrinterWebView;
- PrinterWebViewHandler · class · L15-L29 — class PrinterWebViewHandler
- PrinterWebViewHandler · function · L17-L17 — explicit PrinterWebViewHandler(PrinterWebView& owner);
- on_loaded · function · L20-L20 — virtual void on_loaded(wxWebViewEvent &evt);
- on_script_message · function · L21-L21 — virtual void on_script_message(wxWebViewEvent &evt);
- owner · function · L24-L24 — PrinterWebView& owner() const;
- browser · function · L25-L25 — wxWebView*      browser() const;
- create_printer_webview_handler · function · L31-L31 — std::unique_ptr<PrinterWebViewHandler> create_printer_webview_handler(PrinterWebView& owner);
