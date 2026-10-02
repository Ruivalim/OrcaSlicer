# src/slic3r/GUI/dark_mode/dark_mode.hpp

- IMMERSIVE_HC_CACHE_MODE · type · L12-L16 — enum IMMERSIVE_HC_CACHE_MODE
- PreferredAppMode · type · L19-L26 — enum PreferredAppMode
- WINDOWCOMPOSITIONATTRIB · type · L28-L58 — enum WINDOWCOMPOSITIONATTRIB
- WINDOWCOMPOSITIONATTRIBDATA · class · L60-L65 — struct WINDOWCOMPOSITIONATTRIBDATA
- AllowDarkModeForWindow · function · L105-L110 — bool AllowDarkModeForWindow(HWND hWnd, bool allow)
- IsHighContrast · function · L112-L118 — bool IsHighContrast()
- RefreshTitleBarThemeColor · function · L120-L136 — void RefreshTitleBarThemeColor(HWND hWnd)
- IsColorSchemeChangeMessage · function · L138-L148 — bool IsColorSchemeChangeMessage(LPARAM lParam)
- IsColorSchemeChangeMessage · function · L150-L155 — bool IsColorSchemeChangeMessage(UINT message, LPARAM lParam)
- AllowDarkModeForApp · function · L157-L163 — void AllowDarkModeForApp(bool allow)
- EnableDarkScrollBarForWindowAndChildren · function · L170-L174 — void EnableDarkScrollBarForWindowAndChildren(HWND hwnd)
- lock · function · L172-L172 — std::lock_guard<std::mutex> lock(g_darkScrollBarMutex);
- IsWindowOrParentUsingDarkScrollBar · function · L176-L189 — bool IsWindowOrParentUsingDarkScrollBar(HWND hwnd)
- lock · function · L180-L180 — std::lock_guard<std::mutex> lock(g_darkScrollBarMutex);
- FixDarkScrollBar · function · L191-L219 — void FixDarkScrollBar()
- CheckBuildNumber · function · L221-L227 — constexpr bool CheckBuildNumber(DWORD buildNumber)
- InitDarkMode · function · L229-L275 — void InitDarkMode()
