# src/slic3r/GUI/MediaPlayCtrl.h

- SetMachineObject · function · L37-L37 — void SetMachineObject(MachineObject * obj);
- IsStreaming · function · L39-L39 — bool IsStreaming() const;
- ToggleStream · function · L39-L41 — bool IsStreaming() const;
- msw_rescale · function · L43-L43 — void msw_rescale();
- jump_to_play · function · L45-L45 — void jump_to_play();
- onStateChanged · function · L48-L48 — void onStateChanged(wxMediaEvent & event);
- Play · function · L50-L50 — void Play();
- Stop · function · L52-L52 — void Stop(wxString const &msg = {}, wxString const &msg2 = {});
- TogglePlay · function · L54-L54 — void TogglePlay();
- SetStatus · function · L56-L56 — void SetStatus(wxString const &msg, bool hyperlink = true);
- load · function · L59-L59 — void load();
- on_show_hide · function · L61-L61 — void on_show_hide(wxShowEvent & evt);
- media_proc · function · L63-L63 — void media_proc();
- start_stream_service · function · L65-L65 — static bool start_stream_service(bool *need_install = nullptr);
- get_stream_url · function · L67-L67 — static bool get_stream_url(std::string *url = nullptr);
