# src/slic3r/GUI/Jobs/OAuthJob.hpp

- Plater · class · L13-L13 — class Plater;
- OAuthParams · class · L15-L28 — struct OAuthParams
- OAuthResult · class · L30-L36 — struct OAuthResult
- OAuthData · class · L38-L42 — struct OAuthData
- OAuthJob · class · L44-L59 — class OAuthJob : public Job
- OAuthJob · function · L51-L51 — explicit OAuthJob(const OAuthData& input);
- process · function · L53-L53 — void process(Ctl& ctl) override;
- finalize · function · L54-L54 — void finalize(bool canceled, std::exception_ptr& e) override;
- set_event_handle · function · L56-L56 — void set_event_handle(wxWindow* hanle) { m_event_handle = hanle; }
- parse_token_response · function · L58-L58 — static void parse_token_response(const std::string& body, bool error, OAuthResult& result);
