# src/dev-utils/BaseException.h

- OutputString · function · L12-L12 — virtual void OutputString(LPCTSTR lpszFormat, ...);
- ShowLoadModules · function · L13-L13 — virtual void ShowLoadModules();
- GetCurrentThread · function · L14-L14 — virtual void ShowCallstack(HANDLE hThread = GetCurrentThread(), const CONTEXT* context = NULL);
- ShowCallstack · function · L14-L14 — virtual void ShowCallstack(HANDLE hThread = GetCurrentThread(), const CONTEXT* context = NULL);
- ShowExceptionResoult · function · L15-L15 — virtual void ShowExceptionResoult(DWORD dwExceptionCode);
- GetLogicalAddress · function · L16-L16 — virtual BOOL GetLogicalAddress(PVOID addr, PTSTR szModule, DWORD len, DWORD& section, DWORD& offset );
- ShowRegistorInformation · function · L17-L17 — virtual void ShowRegistorInformation(PCONTEXT pCtx);
- ShowExceptionInformation · function · L18-L18 — virtual void ShowExceptionInformation();
- UnhandledExceptionFilter · function · L19-L19 — static LONG WINAPI UnhandledExceptionFilter(PEXCEPTION_POINTERS pExceptionInfo);
- UnhandledExceptionFilter2 · function · L20-L20 — static LONG WINAPI UnhandledExceptionFilter2(PEXCEPTION_POINTERS pExceptionInfo);
- STF · function · L21-L21 — static void STF(unsigned int ui,  PEXCEPTION_POINTERS pEp);
- set_log_folder · function · L23-L23 — static void set_log_folder(std::string log_folder);
