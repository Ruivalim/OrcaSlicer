# src/libslic3r/clonable_ptr.hpp

- clonable_ptr · class · L26-L140 — template<class T>
- element_type · type · L31-L31 — typedef T element_type;
- clonable_ptr · function · L34-L37 — clonable_ptr() noexcept :
- clonable_ptr · function · L39-L42 — explicit clonable_ptr(T* p) noexcept :
- clonable_ptr · function · L44-L47 — clonable_ptr(const clonable_ptr& rhs) :
- clonable_ptr · function · L49-L53 — clonable_ptr(clonable_ptr&& rhs) noexcept :
- reset · function · L75-L78 — inline void reset() noexcept
- reset · function · L80-L85 — void reset(T* p) noexcept
- swap · function · L88-L93 — void swap(clonable_ptr& rhs) noexcept
- release · function · L96-L99 — inline void release() noexcept
- get · function · L118-L118 — inline T* get()  const noexcept
- destroy · function · L126-L130 — inline void destroy() noexcept
- release · function · L133-L136 — inline void release() const noexcept
