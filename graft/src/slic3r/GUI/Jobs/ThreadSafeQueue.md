# src/slic3r/GUI/Jobs/ThreadSafeQueue.hpp

- BlockingWait · class · L14-L23 — struct BlockingWait
- ThreadSafeQueueSPSC · class · L26-L120 — template<class T,
- consume_one · function · L37-L70 — template<class Fn> bool consume_one(const BlockingWait &blkw, Fn &&fn)
- consume_one · function · L73-L92 — template<class Fn> bool consume_one(Fn &&fn)
- push · function · L95-L100 — template<class...TArgs> void push(TArgs&&...el)
- empty · function · L102-L106 — bool empty() const
- size · function · L108-L112 — size_t size() const
- clear · function · L114-L119 — void clear()
