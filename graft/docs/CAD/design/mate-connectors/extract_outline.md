# docs/CAD/design/mate-connectors/extract_outline.py

- wire_pts · function · L30-L48 — def wire_pts(w, tol=0.05): # ORDER MATTERS and w.Edges does not carry it: OCC hands the edges back in whatever order the # face stored them, so concatenating their discretisations gives a scrambled ring. The first # version of this script did exactly that and emitted an outline with 7 duplicated points and # twice the perimeter it should have. OrderedEdges walks the wire, and each edge is reversed # when its own orientation runs against the walk.
