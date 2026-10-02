# deps_src/glu-libtess/src/priorityq-heap.h

- PQhandle · type · L80-L80 — typedef long PQhandle;
- PriorityQ · type · L81-L81 — typedef struct PriorityQ PriorityQ;
- PQnode · type · L83-L83 — typedef struct { PQhandle handle; } PQnode;
- PQhandleElem · type · L84-L84 — typedef struct { PQkey key; PQhandle node; } PQhandleElem;
- PriorityQ · class · L86-L93 — struct PriorityQ
- pqNewPriorityQ · function · L95-L95 — PriorityQ	*pqNewPriorityQ( int (*leq)(PQkey key1, PQkey key2) );
- pqDeletePriorityQ · function · L96-L96 — void		pqDeletePriorityQ( PriorityQ *pq );
- pqInit · function · L98-L98 — void		pqInit( PriorityQ *pq );
- pqInsert · function · L99-L99 — PQhandle	pqInsert( PriorityQ *pq, PQkey key );
- pqExtractMin · function · L100-L100 — PQkey		pqExtractMin( PriorityQ *pq );
- pqDelete · function · L101-L101 — void		pqDelete( PriorityQ *pq, PQhandle handle );
