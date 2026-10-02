# tests/slic3rutils/test_slicing_pipeline_bindings.cpp

- TestLayerRegion · class · L212-L214 — struct TestLayerRegion : Slic3r::LayerRegion
- TestLayerRegion · function · L213-L213 — TestLayerRegion() : Slic3r::LayerRegion(nullptr, nullptr) {}
- build_nested_perimeters · function · L221-L235 — static void build_nested_perimeters(TestLayerRegion& region)
- pathA · function · L223-L223 — ExtrusionPath pathA(erExternalPerimeter);        // -> "Outer wall"
- pathB · function · L227-L227 — ExtrusionPath pathB(erInternalInfill);           // -> "Sparse infill"
- surf · function · L262-L262 — Slic3r::Surface surf(Slic3r::stInternalSolid);
- build_nested_collection · function · L418-L434 — static Slic3r::ExtrusionEntityCollection build_nested_collection()
- pathA · function · L420-L420 — ExtrusionPath pathA(erExternalPerimeter);        // -> "Outer wall"
- pathB · function · L424-L424 — ExtrusionPath pathB(erInternalInfill);           // -> "Sparse infill"
- TestLayer · class · L497-L500 — struct TestLayer : Slic3r::Layer
- TestLayer · function · L499-L499 — TestLayer() : Slic3r::Layer(0, nullptr, 0.2, 0.45, 0.35) {}
