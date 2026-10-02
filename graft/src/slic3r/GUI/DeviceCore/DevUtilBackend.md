# src/slic3r/GUI/DeviceCore/DevUtilBackend.h

- GetNozzleInfo · function · L37-L37 — static MultiNozzleUtils::NozzleInfo GetNozzleInfo(const DevNozzle& dev_nozzle);
- GetNozzleGroupResult · function · L40-L40 — static std::shared_ptr<MultiNozzleUtils::NozzleGroupResultBase> GetNozzleGroupResult(Slic3r::GUI::Plater *plater);
- CollectNozzleInfo · function · L41-L41 — static std::unordered_map<NozzleDef, int> CollectNozzleInfo(MultiNozzleUtils::NozzleGroupResultBase *nozzle_group_res, int logic_ext_id);
- GetFilamentDryingPreset · function · L44-L44 — static std::optional<DevFilamentDryingPreset> GetFilamentDryingPreset(const std::string& fila_id);
