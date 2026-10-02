# deps_src/mcut/source/preproc.cpp

- client_input_arrays_to_hmesh · function · L21-L318 — bool client_input_arrays_to_hmesh(
- InputStorageIteratorType · type · L117-L117 — typedef std::vector<uint32_t>::const_iterator InputStorageIteratorType;
- OutputStorageType · type · L118-L118 — typedef std::pair<InputStorageIteratorType, InputStorageIteratorType> OutputStorageType; // range of faces
- faces · function · L122-L122 — std::vector<std::vector<vd_t>> faces(numFaces);
- descr · function · L169-L169 — const vertex_descriptor_t descr(idx);
- descr · function · L289-L289 — const vertex_descriptor_t descr(idx); // = fIter->second; //vmap[*fIter.first];
- is_coplanar · function · L320-L349 — bool is_coplanar(const hmesh_t& m, const fd_t& f, int& fv_count)
- check_input_mesh · function · L353-L353 — bool check_input_mesh(std::shared_ptr<context_t>& context_ptr, const hmesh_t& m)
- convert · function · L421-L439 — McResult convert(const status_t& v)
- convert · function · L441-L458 — McPatchLocation convert(const cm_patch_location_t& v)
- convert · function · L460-L477 — McFragmentLocation convert(const sm_frag_location_t& v)
- resolve_floating_polygons · function · L479-L1274 — void resolve_floating_polygons(
- fp_edge_pair_priority_queue · function · L795-L799 — std::priority_queue<
- intersectionPoint · function · L916-L916 — vec2 intersectionPoint(garbageVal);
- aDist · function · L957-L957 — double aDist(std::numeric_limits<double>::max()); // bias toward points inside polygon
- bDist · function · L978-L978 — double bDist(std::numeric_limits<double>::max());
- preproc · function · L1276-L1288 — extern "C" void preproc(
- mersenne_twister_generator · function · L1503-L1503 — static thread_local std::mt19937 mersenne_twister_generator(random_engine());
