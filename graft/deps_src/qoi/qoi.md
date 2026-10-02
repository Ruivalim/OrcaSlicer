# deps_src/qoi/qoi.h

- qoi_desc · type · L256-L261 — typedef struct
- qoi_write · function · L272-L272 — int qoi_write(const char *filename, const void *data, const qoi_desc *desc);
- qoi_read · function · L285-L285 — void *qoi_read(const char *filename, qoi_desc *desc, int channels);
- qoi_encode · function · L298-L298 — void *qoi_encode(const void *data, const qoi_desc *desc, int *out_len);
- qoi_decode · function · L309-L309 — void *qoi_decode(const void *data, int size, qoi_desc *desc, int channels);
- qoi_rgba_t · type · L354-L357 — typedef union
- qoi_write_32 · function · L361-L366 — static void qoi_write_32(unsigned char *bytes, int *p, unsigned int v)
- qoi_read_32 · function · L368-L374 — static unsigned int qoi_read_32(const unsigned char *bytes, int *p)
- qoi_encode · function · L376-L376 — void *qoi_encode(const void *data, const qoi_desc *desc, int *out_len)
- qoi_decode · function · L509-L509 — void *qoi_decode(const void *data, int size, qoi_desc *desc, int channels)
- qoi_write · function · L617-L637 — int qoi_write(const char *filename, const void *data, const qoi_desc *desc)
- qoi_read · function · L639-L639 — void *qoi_read(const char *filename, qoi_desc *desc, int channels)
