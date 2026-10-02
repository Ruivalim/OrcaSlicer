# deps/GLEW/glew/include/GL/wglew.h

- const · type · L140-L140 — typedef HGLRC (WINAPI * PFNWGLCREATEASSOCIATEDCONTEXTATTRIBSAMDPROC) (UINT id, HGLRC hShareContext, const int* attribList);
- const · type · L212-L212 — typedef HGLRC (WINAPI * PFNWGLCREATECONTEXTATTRIBSARBPROC) (HDC hDC, HGLRC hShareContext, const int* attribList);
- const · type · L329-L329 — typedef HPBUFFERARB (WINAPI * PFNWGLCREATEPBUFFERARBPROC) (HDC hDC, int iPixelFormat, int iWidth, int iHeight, const int* piAttribList);
- const · type · L400-L400 — typedef BOOL (WINAPI * PFNWGLCHOOSEPIXELFORMATARBPROC) (HDC hdc, const int* piAttribIList, const FLOAT* pfAttribFList, UINT nMaxFormats, int* piFormats, UINT* nNumFormats);
- const · type · L401-L401 — typedef BOOL (WINAPI * PFNWGLGETPIXELFORMATATTRIBFVARBPROC) (HDC hdc, int iPixelFormat, int iLayerPlane, UINT nAttributes, const int* piAttributes, FLOAT* pfValues);
- const · type · L402-L402 — typedef BOOL (WINAPI * PFNWGLGETPIXELFORMATATTRIBIVARBPROC) (HDC hdc, int iPixelFormat, int iLayerPlane, UINT nAttributes, const int* piAttributes, int* piValues);
- const · type · L655-L655 — typedef HPBUFFEREXT (WINAPI * PFNWGLCREATEPBUFFEREXTPROC) (HDC hDC, int iPixelFormat, int iWidth, int iHeight, const int* piAttribList);
- const · type · L722-L722 — typedef BOOL (WINAPI * PFNWGLCHOOSEPIXELFORMATEXTPROC) (HDC hdc, const int* piAttribIList, const FLOAT* pfAttribFList, UINT nMaxFormats, int* piFormats, UINT* nNumFormats);
- const · type · L780-L780 — typedef BOOL (WINAPI * PFNWGLSETDIGITALVIDEOPARAMETERSI3DPROC) (HDC hDC, int iAttribute, const int* piValue);
- const · type · L799-L799 — typedef BOOL (WINAPI * PFNWGLSETGAMMATABLEI3DPROC) (HDC hDC, int iEntries, const USHORT* puRed, const USHORT* puGreen, const USHORT* puBlue);
- const · type · L800-L800 — typedef BOOL (WINAPI * PFNWGLSETGAMMATABLEPARAMETERSI3DPROC) (HDC hDC, int iAttribute, const int* piValue);
- const · type · L864-L864 — typedef BOOL (WINAPI * PFNWGLASSOCIATEIMAGEBUFFEREVENTSI3DPROC) (HDC hDC, const HANDLE* pEvent, const LPVOID* pAddress, const DWORD* pSize, UINT count);
- UINT · type · L867-L867 — typedef BOOL (WINAPI * PFNWGLRELEASEIMAGEBUFFEREVENTSI3DPROC) (HDC hDC, const LPVOID* pAddress, UINT count);
- _GPU_DEVICE · class · L1010-L1016 — typedef struct _GPU_DEVICE
- wglewInit · function · L1449-L1449 — GLEWAPI GLenum GLEWAPIENTRY wglewInit ();
- wglewIsSupported · function · L1450-L1450 — GLEWAPI GLboolean GLEWAPIENTRY wglewIsSupported (const char *name);
- wglewGetExtension · function · L1460-L1460 — GLEWAPI GLboolean GLEWAPIENTRY wglewGetExtension (const char *name);
