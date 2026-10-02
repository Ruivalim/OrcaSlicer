# src/libslic3r/GCode/OrderingStrategies.hpp

- tsp_2opt_improve · function · L24-L24 — bool tsp_2opt_improve(std::vector<size_t>& path, const Points& centers, int max_passes = 10);
- tsp_remove_crossings · function · L28-L28 — bool tsp_remove_crossings(std::vector<size_t>& path, const Points& centers);
- tsp_rotate_minimize_closing · function · L31-L31 — void tsp_rotate_minimize_closing(std::vector<size_t>& path, const Points& centers);
- tsp_cycle_path_length · function · L34-L43 — inline double tsp_cycle_path_length(const std::vector<size_t>& path, const Points& centers)
- tsp_max_edge_length · function · L46-L56 — inline double tsp_max_edge_length(const std::vector<size_t>& path, const Points& centers)
- chain_instances_with_core · function · L66-L117 — template<typename CoreFn>
- snake_core · function · L124-L124 — std::vector<size_t> snake_core(const Points& centers);
- chain_print_object_instances_snake · function · L131-L131 — std::vector<const PrintInstance*> chain_print_object_instances_snake(const std::vector<const PrintObject*>& print_objects, const Point* start_near);
- chain_print_object_instances_snake · function · L132-L132 — std::vector<const PrintInstance*> chain_print_object_instances_snake(const Print& print);
- chain_print_object_instances_best_of · function · L136-L136 — std::vector<const PrintInstance*> chain_print_object_instances_best_of(const std::vector<const PrintObject*>& print_objects, const Point* start_near);
- chain_print_object_instances_best_of · function · L137-L137 — std::vector<const PrintInstance*> chain_print_object_instances_best_of(const Print& print);
- order_points_with_strategy · function · L142-L142 — std::vector<size_t> order_points_with_strategy(const Points& points, PrintOrder print_order, const Point* start_near);
