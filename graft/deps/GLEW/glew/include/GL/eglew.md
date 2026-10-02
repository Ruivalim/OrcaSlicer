# deps/GLEW/glew/include/GL/eglew.h

- EGLint · type · L119-L119 — typedef int32_t EGLint;
- EGLBoolean · type · L121-L121 — typedef unsigned int EGLBoolean;
- EGLenum · type · L128-L128 — typedef unsigned int EGLenum;
- EGLAttrib · type · L132-L132 — typedef intptr_t EGLAttrib;
- EGLTime · type · L133-L133 — typedef khronos_utime_nanoseconds_t EGLTime;
- EGLAttribKHR · type · L137-L137 — typedef intptr_t EGLAttribKHR;
- EGLTimeKHR · type · L141-L141 — typedef khronos_utime_nanoseconds_t EGLTimeKHR;
- EGLuint64KHR · type · L144-L144 — typedef khronos_uint64_t EGLuint64KHR;
- EGLNativeFileDescriptorKHR · type · L145-L145 — typedef int EGLNativeFileDescriptorKHR;
- EGLsizeiANDROID · type · L146-L146 — typedef khronos_ssize_t EGLsizeiANDROID;
- EGLTimeNV · type · L153-L153 — typedef khronos_utime_nanoseconds_t EGLTimeNV;
- EGLuint64NV · type · L154-L154 — typedef khronos_utime_nanoseconds_t EGLuint64NV;
- EGLnsecsANDROID · type · L155-L155 — typedef khronos_stime_nanoseconds_t EGLnsecsANDROID;
- eglGetProcAddress · function · L172-L172 — EGLAPI __eglMustCastToProperFunctionPointerType EGLAPIENTRY eglGetProcAddress (const char *procname);
- eglewInit · function · L3039-L3039 — GLEWAPI GLenum GLEWAPIENTRY eglewInit (EGLDisplay display);
- eglewIsSupported · function · L3040-L3040 — GLEWAPI GLboolean GLEWAPIENTRY eglewIsSupported (const char *name);
- eglewGetExtension · function · L3045-L3045 — GLEWAPI GLboolean GLEWAPIENTRY eglewGetExtension (const char *name);
