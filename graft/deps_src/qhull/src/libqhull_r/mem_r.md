# deps_src/qhull/src/libqhull_r/mem_r.h

- setT · type · L26-L26 — typedef struct setT setT;          /* defined in qset_r.h */
- qhT · type · L31-L31 — typedef struct qhT qhT;          /* defined in libqhull_r.h */
- ptr_intT · type · L92-L92 — typedef long long ptr_intT;
- ptr_intT · type · L94-L94 — typedef long long ptr_intT;
- ptr_intT · type · L96-L96 — typedef long ptr_intT;
- qhmemT · type · L117-L117 — typedef struct qhmemT qhmemT;
- qhmemT · class · L120-L151 — struct qhmemT {               /* global memory management variables */
- qh_memalloc · function · L218-L218 — void *qh_memalloc(qhT *qh, int insize);
- qh_memcheck · function · L219-L219 — void qh_memcheck(qhT *qh);
- qh_memfree · function · L220-L220 — void qh_memfree(qhT *qh, void *object, int insize);
- qh_memfreeshort · function · L221-L221 — void qh_memfreeshort(qhT *qh, int *curlong, int *totlong);
- qh_meminit · function · L222-L222 — void qh_meminit(qhT *qh, FILE *ferr);
- qh_meminitbuffers · function · L223-L224 — void qh_meminitbuffers(qhT *qh, int tracelevel, int alignment, int numsizes,
- qh_memsetup · function · L225-L225 — void qh_memsetup(qhT *qh);
- qh_memsize · function · L226-L226 — void qh_memsize(qhT *qh, int size);
- qh_memstatistics · function · L227-L227 — void qh_memstatistics(qhT *qh, FILE *fp);
- qh_memtotal · function · L228-L228 — void qh_memtotal(qhT *qh, int *totlong, int *curlong, int *totshort, int *curshort, int *maxlong, int *totbuffer);
