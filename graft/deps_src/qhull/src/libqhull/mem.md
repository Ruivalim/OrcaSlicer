# deps_src/qhull/src/libqhull/mem.h

- ptr_intT · type · L82-L82 — typedef long long ptr_intT;
- ptr_intT · type · L84-L84 — typedef long long ptr_intT;
- ptr_intT · type · L86-L86 — typedef long ptr_intT;
- qhmemT · type · L107-L107 — typedef struct qhmemT qhmemT;
- setT · type · L112-L112 — typedef struct setT setT;          /* defined in qset.h */
- qhmemT · class · L116-L147 — struct qhmemT {               /* global memory management variables */
- qh_memalloc · function · L210-L210 — void *qh_memalloc(int insize);
- qh_memcheck · function · L211-L211 — void qh_memcheck(void);
- qh_memfree · function · L212-L212 — void qh_memfree(void *object, int insize);
- qh_memfreeshort · function · L213-L213 — void qh_memfreeshort(int *curlong, int *totlong);
- qh_meminit · function · L214-L214 — void qh_meminit(FILE *ferr);
- qh_meminitbuffers · function · L215-L216 — void qh_meminitbuffers(int tracelevel, int alignment, int numsizes,
- qh_memsetup · function · L217-L217 — void qh_memsetup(void);
- qh_memsize · function · L218-L218 — void qh_memsize(int size);
- qh_memstatistics · function · L219-L219 — void qh_memstatistics(FILE *fp);
- qh_memtotal · function · L220-L220 — void qh_memtotal(int *totlong, int *curlong, int *totshort, int *curshort, int *maxlong, int *totbuffer);
