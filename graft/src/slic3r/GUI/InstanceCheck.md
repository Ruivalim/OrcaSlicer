# src/slic3r/GUI/InstanceCheck.hpp

- instance_check · function · L25-L25 — bool    instance_check(int argc, char** argv, bool app_config_single_instance);
- send_message_mac · function · L30-L30 — void    send_message_mac(const std::string& msg, const std::string& version);
- send_message_mac_closing · function · L31-L31 — void    send_message_mac_closing(const std::string& msg, const std::string& version);
- unlock_lockfile · function · L34-L34 — bool unlock_lockfile(const std::string& name, const std::string& path);
- MainFrame · class · L39-L39 — class MainFrame;
- OtherInstanceMessageHandler · class · L53-L105 — class OtherInstanceMessageHandler
- OtherInstanceMessageHandler · function · L56-L56 — OtherInstanceMessageHandler() = default;
- OtherInstanceMessageHandler · function · L57-L57 — OtherInstanceMessageHandler(OtherInstanceMessageHandler const&) = delete;
- init · function · L62-L62 — void    init(wxEvtHandler* callback_evt_handler);
- shutdown · function · L64-L64 — void    shutdown(MainFrame* main_frame);
- handle_message · function · L72-L72 — void           handle_message(const std::string& message);
- handle_message_other_closed · function · L75-L75 — void           handle_message_other_closed();
- init_windows_properties · function · L78-L78 — static void    init_windows_properties(MainFrame* main_frame, size_t instance_hash);
- listen · function · L92-L92 — void    listen();
- register_for_messages · function · L97-L97 — void    register_for_messages(const std::string &version_hash);
- unregister_for_messages · function · L98-L98 — void    unregister_for_messages();
- bring_instance_forward · function · L102-L102 — void    bring_instance_forward();
