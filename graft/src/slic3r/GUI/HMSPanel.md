# src/slic3r/GUI/HMSPanel.hpp

- HMSNotifyItem · class · L17-L43 — class HMSNotifyItem : public wxPanel
- init_bitmaps · function · L35-L35 — void          init_bitmaps();
- get_notify_bitmap · function · L36-L36 — wxBitmap &    get_notify_bitmap();
- HMSNotifyItem · function · L39-L39 — HMSNotifyItem(const std::string& dev_id, wxWindow *parent, DevHMSItem& item);
- msw_rescale · function · L42-L42 — void msw_rescale() {}
- HMSPanel · class · L46-L74 — class HMSPanel : public wxPanel
- append_hms_panel · function · L54-L54 — void append_hms_panel(const std::string& dev_id, DevHMSItem &item);
- delete_hms_panels · function · L55-L55 — void delete_hms_panels();
- HMSPanel · function · L59-L59 — HMSPanel(wxWindow *parent, wxWindowID id = wxID_ANY, const wxPoint &pos = wxDefaultPosition, const wxSize &size = wxDefaultSize, long style = wxTAB_TRAVERSAL);
- msw_rescale · function · L62-L62 — void msw_rescale() {}
- Show · function · L64-L64 — bool Show(bool show = true) override;
- update · function · L66-L66 — void update(MachineObject *obj_);
- show_status · function · L68-L68 — void show_status(int status);
- clear_hms_tag · function · L70-L70 — void clear_hms_tag();
