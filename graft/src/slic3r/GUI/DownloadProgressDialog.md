# src/slic3r/GUI/DownloadProgressDialog.hpp

- wxBoxSizer · class · L22-L22 — class wxBoxSizer;
- wxCheckBox · class · L23-L23 — class wxCheckBox;
- wxStaticBitmap · class · L24-L24 — class wxStaticBitmap;
- DownloadProgressDialog · class · L34-L57 — class DownloadProgressDialog : public DPIDialog
- Show · function · L37-L37 — bool Show(bool show) override;
- on_close · function · L38-L38 — void on_close(wxCloseEvent& event);
- DownloadProgressDialog · function · L41-L41 — DownloadProgressDialog(wxString title);
- format_text · function · L42-L42 — wxString format_text(wxStaticText* st, wxString str, int warp);
- on_dpi_changed · function · L45-L45 — void on_dpi_changed(const wxRect &suggested_rect) override;
- update_release_note · function · L46-L46 — void update_release_note(std::string release_note, std::string version);
- make_job · function · L55-L55 — virtual std::unique_ptr<UpgradeNetworkJob> make_job();
- on_finish · function · L56-L56 — virtual void                               on_finish();
