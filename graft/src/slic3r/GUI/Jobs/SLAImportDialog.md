# src/slic3r/GUI/Jobs/SLAImportDialog.hpp

- SLAImportDialog · class · L24-L96 — class SLAImportDialog : public wxDialog, public SLAImportJobView
- SLAImportDialog · function · L30-L75 — SLAImportDialog(Plater *plater) : wxDialog{plater, wxID_ANY, "Import SLA archive"}
- get_selection · function · L77-L81 — Sel get_selection() const override
- get_marchsq_windowsize · function · L83-L93 — Vec2i32 get_marchsq_windowsize() const override
- get_path · function · L95-L95 — std::string get_path() const override { return m_filepicker->GetPath().ToUTF8().data(); }
