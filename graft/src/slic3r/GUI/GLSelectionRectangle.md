# src/slic3r/GUI/GLSelectionRectangle.hpp

- GLCanvas3D · class · L11-L11 — class GLCanvas3D;
- GLSelectionRectangle · class · L13-L53 — class GLSelectionRectangle
- EState · type · L15-L19 — enum EState
- start_dragging · function · L22-L22 — void start_dragging(const Vec2d& mouse_position, EState state);
- dragging · function · L25-L25 — void dragging(const Vec2d& mouse_position);
- contains · function · L29-L29 — std::vector<unsigned int> contains(const std::vector<Vec3d>& points) const;
- stop_dragging · function · L32-L32 — void stop_dragging();
- render · function · L34-L34 — void render(const GLCanvas3D& canvas);
- is_dragging · function · L36-L36 — bool is_dragging() const { return m_state != Off; }
- get_state · function · L37-L37 — EState get_state() const { return m_state; }
- get_width · function · L39-L39 — float get_width() const  { return std::abs(m_start_corner.x() - m_end_corner.x()); }
- get_height · function · L40-L40 — float get_height() const { return std::abs(m_start_corner.y() - m_end_corner.y()); }
- get_left · function · L41-L41 — float get_left() const   { return std::min(m_start_corner.x(), m_end_corner.x()); }
- get_right · function · L42-L42 — float get_right() const  { return std::max(m_start_corner.x(), m_end_corner.x()); }
- get_top · function · L43-L43 — float get_top() const    { return std::max(m_start_corner.y(), m_end_corner.y()); }
- get_bottom · function · L44-L44 — float get_bottom() const { return std::min(m_start_corner.y(), m_end_corner.y()); }
