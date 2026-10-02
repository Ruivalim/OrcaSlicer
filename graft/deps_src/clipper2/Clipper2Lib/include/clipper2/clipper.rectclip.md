# deps_src/clipper2/Clipper2Lib/include/clipper2/clipper.rectclip.h

- class · type · L23-L82 — enum class Location { Left, Top, Right, Bottom, Inside };
- OutPt2List · type · L26-L26 — typedef std::vector<OutPt2*> OutPt2List;
- ExecuteInternal · function · L43-L43 — void ExecuteInternal(const Path64& path);
- GetPath · function · L44-L44 — Path64 GetPath(OutPt2*& op);
- CheckEdges · function · L54-L54 — void CheckEdges();
- TidyEdges · function · L55-L55 — void TidyEdges(size_t idx, OutPt2List& cw, OutPt2List& ccw);
- GetNextLocation · function · L56-L57 — void GetNextLocation(const Path64& path,
- Add · function · L58-L58 — OutPt2* Add(Point64 pt, bool start_new = false);
- AddCorner · function · L59-L59 — void AddCorner(Location prev, Location curr);
- AddCorner · function · L60-L60 — void AddCorner(Location& loc, bool isClockwise);
- RectClip64 · function · L62-L63 — explicit RectClip64(const Rect64& rect) :
- Execute · function · L66-L66 — Paths64 Execute(const Paths64& paths);
- ExecuteInternal · function · L75-L75 — void ExecuteInternal(const Path64& path);
- GetPath · function · L76-L76 — Path64 GetPath(OutPt2*& op);
- RectClipLines64 · function · L78-L78 — explicit RectClipLines64(const Rect64& rect) : RectClip64(rect) {};
- Execute · function · L79-L79 — Paths64 Execute(const Paths64& paths);
