# docs/CAD/design/mate-connectors/glyph_probe.py

- add · function · L34-L41 — def add(name, shape, color, transparency=0)
- frame · function · L43-L52 — def frame(origin, zdir, xdir)
- ring · function · L62-L64 — def ring(t=None)
- quadrant · function · L66-L68 — def quadrant(t=None)
- stem · function · L70-L71 — def stem(L=None, r=None)
- solid_head · function · L73-L74 — def solid_head()
- shell_head · function · L76-L79 — def shell_head()
- short_axis · function · L81-L83 — def short_axis(direction, L=None)
- place · function · L85-L88 — def place(shape, m)
- variant_A · function · L91-L97 — def variant_A(tag, origin): # Onshape baseline
- variant_B · function · L99-L103 — def variant_B(tag, origin, zdir=(0, 0, 1)): # solid cone = driven
- variant_C · function · L105-L109 — def variant_C(tag, origin, zdir=(0, 0, 1)): # hollow collar = fixed
- variant_D_pin · function · L111-L117 — def variant_D_pin(tag, origin, zdir=(0, 0, 1)): # polarity by relief: raised PIN
- variant_D_cup · function · L119-L125 — def variant_D_cup(tag, origin, zdir=(0, 0, 1)): # polarity by relief: sunk CUP
