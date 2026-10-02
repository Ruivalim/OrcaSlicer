# deps_src/libigl/igl/WindingNumberTree.h

- Scalar · type · L36-L38 — typedef
- Index · type · L39-L41 — typedef
- WindingNumberTree · function · L66-L66 — inline virtual ~WindingNumberTree();
- delete_children · function · L67-L67 — inline void delete_children();
- set_mesh · function · L69-L71 — inline void set_mesh(
- set_method · function · L73-L73 — inline void set_method( const WindingNumberMethod & m);
- grow · function · L76-L76 — inline virtual void grow();
- inside · function · L82-L82 — inline virtual bool inside(const Point & p) const;
- winding_number · function · L89-L89 — inline Scalar winding_number(const Point & p) const;
- winding_number_all · function · L92-L92 — inline Scalar winding_number_all(const Point & p) const;
- winding_number_boundary · function · L94-L94 — inline Scalar winding_number_boundary(const Point & p) const;
- print · function · L111-L111 — inline void print(const char * tab="");
- set_mesh · function · L183-L185 — inline void igl::WindingNumberTree<Scalar,Index>::set_mesh(
- delete_children · function · L225-L225 — inline void igl::WindingNumberTree<Scalar,Index>::delete_children()
- set_method · function · L240-L240 — inline void igl::WindingNumberTree<Scalar,Index>::set_method(const WindingNumberMethod & m)
- set_method · function · L243-L245 — for(auto child : children)
- this_that · function · L440-L440 — pair<const WindingNumberTree*,const WindingNumberTree*> this_that(this,&that);
