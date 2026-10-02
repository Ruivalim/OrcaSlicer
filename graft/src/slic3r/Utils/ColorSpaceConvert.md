# src/slic3r/Utils/ColorSpaceConvert.hpp

- rgb_to_yuv · function · L8-L8 — std::tuple<int, int, int> rgb_to_yuv(float r, float g, float b);
- PivotRGB · function · L9-L9 — double PivotRGB(double n);
- PivotXYZ · function · L10-L10 — double PivotXYZ(double n);
- XYZ2RGB · function · L11-L11 — void XYZ2RGB(float X, float Y, float Z, float* R, float* G, float* B);
- Lab2XYZ · function · L12-L12 — void Lab2XYZ(float L, float a, float b, float* X, float* Y, float* Z);
- Lab2RGB · function · L13-L13 — void Lab2RGB(float L, float a, float b, float* R, float* G, float* B);
- RGB2XYZ · function · L14-L14 — void RGB2XYZ(float R, float G, float B, float* X, float* Y, float* Z);
- XYZ2Lab · function · L15-L15 — void XYZ2Lab(float X, float Y, float Z, float* L, float* a, float* b);
- RGB2Lab · function · L16-L16 — void RGB2Lab(float R, float G, float B, float* L, float* a, float* b);
- RGB2HSV · function · L17-L17 — void RGB2HSV(float r, float g, float b, float* h, float* s, float* v);
- DeltaE00 · function · L19-L19 — float DeltaE00(float l1, float a1, float b1, float l2, float a2, float b2);
- DeltaE94 · function · L20-L20 — float DeltaE94(float l1, float a1, float b1, float l2, float a2, float b2);
- DeltaE76 · function · L21-L21 — float DeltaE76(float l1, float a1, float b1, float l2, float a2, float b2);
- wxColour · class · L23-L23 — class wxColour;
- color_to_string · function · L24-L24 — std::string color_to_string(const wxColour &color);
- string_to_wxColor · function · L25-L25 — wxColour    string_to_wxColor(const std::string &str);
