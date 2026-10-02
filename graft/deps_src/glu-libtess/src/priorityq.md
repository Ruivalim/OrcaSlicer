# deps_src/glu-libtess/src/priorityq.h

- PQkey · type · L93-L93 — typedef PQHeapKey PQkey;
- PQhandle · type · L94-L94 — typedef PQHeapHandle PQhandle;
- PriorityQ · type · L95-L95 — typedef struct PriorityQ PriorityQ;
- PriorityQ · class · L97-L104 — struct PriorityQ
- pqNewPriorityQ · function · L106-L106 — PriorityQ	*pqNewPriorityQ( int (*leq)(PQkey key1, PQkey key2) );
- pqDeletePriorityQ · function · L107-L107 — void		pqDeletePriorityQ( PriorityQ *pq );
- pqInit · function · L109-L109 — int		pqInit( PriorityQ *pq );
- pqInsert · function · L110-L110 — PQhandle	pqInsert( PriorityQ *pq, PQkey key );
- pqExtractMin · function · L111-L111 — PQkey		pqExtractMin( PriorityQ *pq );
- pqDelete · function · L112-L112 — void		pqDelete( PriorityQ *pq, PQhandle handle );
- pqMinimum · function · L114-L114 — PQkey		pqMinimum( PriorityQ *pq );
- pqIsEmpty · function · L115-L115 — int		pqIsEmpty( PriorityQ *pq );
