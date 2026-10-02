# deps_src/qhull/src/libqhullcpp/RboxPoints.h

- qh_fprintf_rbox · function · L39-L39 — friend void ::qh_fprintf_rbox(qhT *qh, FILE *fp, int msgcode, const char *fmt, ... );
- RboxPoints · function · L44-L44 — explicit            RboxPoints(const char *rboxCommand);
- allocateQhullQh · function · L50-L50 — void                allocateQhullQh();
- clearRboxMessage · function · L54-L54 — void                clearRboxMessage();
- newCount · function · L55-L55 — countT              newCount() const { return rbox_new_count; }
- rboxMessage · function · L56-L56 — std::string         rboxMessage() const;
- rboxStatus · function · L57-L64 — int                 rboxStatus() const;
- hasRboxMessage · function · L58-L58 — bool                hasRboxMessage() const;
- setNewCount · function · L59-L59 — void                setNewCount(countT pointCount) { QHULL_ASSERT(pointCount>=0); rbox_new_count= pointCount; }
- reservePoints · function · L64-L64 — void                reservePoints() { reserveCoordinates((count()+newCount())*dimension()); }
