# src/slic3r/GUI/ProcessRunner.hpp

- ProcessRunner · class · L19-L89 — class ProcessRunner : public wxEvtHandler
- ProcessRunner · function · L22-L22 — ProcessRunner();
- OutputLine · class · L25-L28 — struct OutputLine
- run_command_line_async · function · L37-L39 — bool run_command_line_async(const std::string& command_line,
- SyncResult · class · L41-L45 — struct SyncResult
- run_sync · function · L49-L50 — static SyncResult run_sync(const std::string& executable,
- write_stdin · function · L53-L53 — void write_stdin(const std::string& data);
- is_running · function · L56-L56 — bool is_running() const;
- terminate · function · L59-L59 — void terminate();
- on_timer · function · L62-L62 — void on_timer(wxTimerEvent& event);
- finish_process · function · L63-L63 — void finish_process(int exit_code);
- start_reader_threads · function · L64-L64 — void start_reader_threads();
- join_reader_threads · function · L65-L65 — void join_reader_threads();
- enqueue_output · function · L66-L66 — void enqueue_output(std::string line, bool is_stderr);
- drain_output_queue · function · L67-L67 — std::vector<OutputLine> drain_output_queue();
- join_launch_thread · function · L69-L69 — void join_launch_thread();
