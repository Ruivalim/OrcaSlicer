# src/slic3r/GUI/ImageDPIFrame.hpp

- wxStaticBitmap · class · L9-L9 — class wxStaticBitmap;
- ImageDPIFrame · class · L11-L38 — class ImageDPIFrame : public Slic3r::GUI::DPIFrame
- ImageDPIFrame · function · L14-L14 — ImageDPIFrame();
- on_dpi_changed · function · L16-L16 — void on_dpi_changed(const wxRect &suggested_rect) override;
- sys_color_changed · function · L17-L17 — void sys_color_changed();
- on_show · function · L18-L18 — void on_show();
- on_hide · function · L19-L19 — void on_hide();
- Show · function · L20-L20 — bool Show(bool show = true) override;
- set_bitmap · function · L22-L22 — void set_bitmap(const wxBitmap& bit_map);
- get_image_px · function · L23-L23 — int  get_image_px() { return m_image_px; }
- set_title · function · L24-L24 — void set_title(const wxString& title);
- init_timer · function · L27-L27 — void init_timer();
- on_timer · function · L28-L28 — void on_timer(wxTimerEvent &event);
