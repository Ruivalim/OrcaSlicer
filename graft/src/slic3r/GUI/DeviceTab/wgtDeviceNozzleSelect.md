# src/slic3r/GUI/DeviceTab/wgtDeviceNozzleSelect.h

- GetSelectedNozzlePosID · function · L40-L40 — int  GetSelectedNozzlePosID() const { return m_selected_nozzle.GetNozzlePosId();}
- UpdatSelectedNozzles · function · L41-L41 — void UpdatSelectedNozzles(std::shared_ptr<DevNozzleRack> rack, std::vector<int> selected_nozzle_pos_vec, bool use_dynamic_switch, std::optional<PrintFromType> print_from_type);// for slicing with dynamic switch
- Rescale · function · L42-L42 — void Rescale();
- CreateGui · function · L45-L45 — void CreateGui();
- ClearSelection · function · L47-L47 — void ClearSelection();
- SetSelectedNozzle · function · L48-L48 — void SetSelectedNozzle(const DevNozzle &nozzle);
- UpdatSelectedNozzle · function · L49-L49 — void UpdatSelectedNozzle(std::shared_ptr<DevNozzleRack> rack, int selected_nozzle_pos_id = -1); // for slicing without dynamic switch
- UpdateNozzleInfos · function · L51-L51 — void UpdateNozzleInfos(std::shared_ptr<DevNozzleRack> rack);
- OnNozzleItemSelected · function · L53-L53 — void OnNozzleItemSelected(wxCommandEvent& evt);
