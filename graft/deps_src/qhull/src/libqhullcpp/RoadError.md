# deps_src/qhull/src/libqhullcpp/RoadError.h

- clearGlobalLog · function · L65-L65 — static void         clearGlobalLog() { global_log.seekp(0); }
- emptyGlobalLog · function · L66-L66 — static bool         emptyGlobalLog() { return global_log.tellp()<=0; }
- stringGlobalLog · function · L67-L67 — static const char  *stringGlobalLog() { return global_log.str().c_str(); }
- what · function · L70-L70 — virtual const char *what() const throw();
- isValid · function · L73-L73 — bool                isValid() const { return log_event.isValid(); }
- errorCode · function · L74-L74 — int                 errorCode() const { return error_code; };
- roadLogEvent · function · L76-L76 — RoadLogEvent        roadLogEvent() const { return log_event; };
- logErrorLastResort · function · L79-L79 — void                logErrorLastResort() const;
