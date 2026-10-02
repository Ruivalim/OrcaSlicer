# src/slic3r/GUI/Widgets/StateHandler.hpp

- StateHandler · class · L11-L62 — class StateHandler : public wxEvtHandler
- State · type · L14-L25 — enum State
- StateHandler · function · L28-L28 — StateHandler(wxWindow * owner);
- attach · function · L33-L33 — void attach(StateColor const & color);
- attach · function · L35-L35 — void attach(std::vector<StateColor const *> const & colors);
- attach_child · function · L37-L37 — void attach_child(wxWindow *child);
- remove_child · function · L39-L39 — void remove_child(wxWindow *child);
- update_binds · function · L41-L41 — void update_binds();
- states · function · L43-L43 — int states() const { return states_ | states2_; }
- set_state · function · L45-L45 — void set_state(int state, int mask);
- StateHandler · function · L48-L48 — StateHandler(StateHandler * parent, wxWindow *owner);
- changed · function · L50-L50 — void changed(wxEvent &event);
- changed · function · L52-L52 — void changed(int state2);
