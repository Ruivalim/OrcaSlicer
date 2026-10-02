# src/slic3r/plugin/pluginTypes/slicingPipeline/SlicingPipelinePluginCapability.hpp

- SlicingPipelineContext · class · L16-L32 — struct SlicingPipelineContext
- cancelled · function · L31-L31 — bool cancelled() const;                     // -> print->canceled() (false when print is null)
- SlicingPipelinePluginCapability · class · L34-L41 — class SlicingPipelinePluginCapability : public PluginCapabilityInterface
- get_type · function · L36-L36 — PluginCapabilityType get_type() const override { return PluginCapabilityType::SlicingPipeline; }
- execute · function · L39-L39 — virtual ExecutionResult execute(SlicingPipelineContext& ctx) = 0;
- RegisterBindings · function · L40-L40 — static void RegisterBindings(pybind11::module_& module);
