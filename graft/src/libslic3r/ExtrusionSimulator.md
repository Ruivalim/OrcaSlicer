# src/libslic3r/ExtrusionSimulator.hpp

- ExtrusionSimulationType · type · L10-L17 — enum ExtrusionSimulationType
- ExtrusionSimulatorImpl · class · L20-L20 — class ExtrusionSimulatorImpl;
- ExtrusionSimulator · class · L22-L55 — class ExtrusionSimulator
- ExtrusionSimulator · function · L25-L25 — ExtrusionSimulator();
- set_image_size · function · L31-L31 — void  		set_image_size(const Point &image_size);
- set_viewport · function · L33-L33 — void  		set_viewport(const BoundingBox &viewport);
- set_bounding_box · function · L35-L35 — void		set_bounding_box(const BoundingBox &bbox);
- reset_accumulator · function · L38-L38 — void		reset_accumulator();
- extrude_to_accumulator · function · L42-L42 — void		extrude_to_accumulator(const ExtrusionPath &path, const Point &shift, ExtrusionSimulationType simulationType);
- evaluate_accumulator · function · L45-L45 — void		evaluate_accumulator(ExtrusionSimulationType simulationType);
- image_ptr · function · L47-L47 — const void* image_ptr() const;
