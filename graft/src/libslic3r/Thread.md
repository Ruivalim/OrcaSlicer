# src/libslic3r/Thread.hpp

- set_thread_name · function · L22-L22 — bool set_thread_name(std::thread &thread, const char *thread_name);
- set_thread_name · function · L23-L23 — inline bool set_thread_name(std::thread &thread, const std::string &thread_name) { return set_thread_name(thread, thread_name.c_str()); }
- set_thread_name · function · L24-L24 — bool set_thread_name(boost::thread &thread, const char *thread_name);
- set_thread_name · function · L25-L25 — inline bool set_thread_name(boost::thread &thread, const std::string &thread_name) { return set_thread_name(thread, thread_name.c_str()); }
- set_current_thread_name · function · L26-L26 — bool set_current_thread_name(const char *thread_name);
- set_current_thread_name · function · L27-L27 — inline bool set_current_thread_name(const std::string &thread_name) { return set_current_thread_name(thread_name.c_str()); }
- save_main_thread_id · function · L30-L30 — void save_main_thread_id();
- get_main_thread_id · function · L32-L32 — boost::thread::id get_main_thread_id();
- is_main_thread_active · function · L34-L34 — bool is_main_thread_active();
- get_current_thread_name · function · L39-L39 — std::optional<std::string> get_current_thread_name();
- name_tbb_thread_pool_threads_set_locale · function · L44-L44 — void name_tbb_thread_pool_threads_set_locale();
- create_thread · function · L46-L67 — template<class Fn>
- create_thread · function · L69-L73 — template<class Fn> inline boost::thread create_thread(Fn &&fn)
