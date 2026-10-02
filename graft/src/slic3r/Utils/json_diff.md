# src/slic3r/Utils/json_diff.hpp

- json_diff · class · L14-L40 — class json_diff
- diff_objects · function · L26-L26 — int  diff_objects(json const &in, json &out, json const &base);
- restore_objects · function · L27-L27 — int  restore_objects(json const &in, json &out, json const &base);
- restore_append_objects · function · L28-L28 — int  restore_append_objects(json const &in, json &out);
- merge_objects · function · L29-L29 — void merge_objects(json const &in, json &out);
- load_compatible_settings · function · L32-L32 — bool load_compatible_settings(std::string const &type, std::string const &version);
- all2diff · function · L33-L33 — int all2diff(json const &in, json &out);
- diff2all · function · L34-L34 — int  diff2all(json const &in, json &out);
- all2diff_base_reset · function · L35-L35 — int  all2diff_base_reset(json const &base);
- diff2all_base_reset · function · L36-L36 — int  diff2all_base_reset(json &base);
- compare_print · function · L37-L37 — void compare_print(json &a, json &b);
- is_need_request · function · L39-L39 — bool is_need_request();
