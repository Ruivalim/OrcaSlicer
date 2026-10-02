# deps_src/nlohmann/detail/input/parser.hpp

- parse_event_t · type · L26-L40 — enum class parse_event_t : std::uint8_t
- parser · class · L51-L496 — template<typename BasicJsonType, typename InputAdapterType>
- parser · function · L63-L73 — explicit parser(InputAdapterType&& adapter,
- parse · function · L85-L137 — void parse(const bool strict, BasicJsonType& result)
- sdp · function · L89-L89 — json_sax_dom_callback_parser<BasicJsonType> sdp(result, callback, allow_exceptions);
- sdp · function · L117-L117 — json_sax_dom_parser<BasicJsonType> sdp(result, allow_exceptions);
- accept · function · L145-L149 — bool accept(const bool strict = true)
- sax_parse · function · L153-L153 — bool sax_parse(SAX* sax, const bool strict = true)
- sax_parse_internal · function · L170-L450 — template<typename SAX>
- get_token · function · L453-L456 — token_type get_token()
- exception_message · function · L458-L485 — std::string exception_message(const token_type expected, const std::string& context)
