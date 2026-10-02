# src/slic3r/GUI/Jobs/Worker.hpp

- Worker · class · L13-L50 — class Worker
- push · function · L17-L17 — virtual bool push(std::shared_ptr<Job> job) = 0;
- is_idle · function · L22-L22 — virtual bool is_idle() const = 0;
- cancel · function · L28-L28 — virtual void cancel() = 0;
- cancel_all · function · L31-L31 — virtual void cancel_all() = 0;
- process_events · function · L36-L36 — virtual void process_events() = 0;
- wait_for_current_job · function · L41-L41 — virtual bool wait_for_current_job(unsigned timeout_ms = 0) = 0;
- wait_for_idle · function · L46-L46 — virtual bool wait_for_idle(unsigned timeout_ms = 0) = 0;
- queue_job · function · L56-L78 — template<class ProcessFn, class FinishFn,
- LambdaJob · class · L61-L74 — struct LambdaJob: Job
- LambdaJob · function · L65-L67 — LambdaJob(ProcessFn pfn, FinishFn ffn)
- process · function · L69-L69 — void process(Ctl &ctl) override { fn(ctl); }
- finalize · function · L70-L73 — void finalize(bool canceled, std::exception_ptr &eptr) override
- queue_job · function · L80-L84 — template<class ProcessFn, class = std::enable_if_t<IsProcessFn<ProcessFn>>>
- queue_job · function · L86-L89 — inline bool queue_job(Worker &w, std::shared_ptr<Job> j)
- replace_job · function · L96-L100 — template<class...Args> bool replace_job(Worker &w, Args&& ...args)
- stop_current_job · function · L103-L107 — inline bool stop_current_job(Worker &w, unsigned timeout_ms = 0)
- stop_queue · function · L111-L115 — inline bool stop_queue(Worker &w, unsigned timeout_ms = 0)
