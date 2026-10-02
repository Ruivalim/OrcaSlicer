# deps_src/qhull/src/libqhullcpp/QhullFacetSet.h

- QhullFacetSetIterator · type · L25-L25 — typedef QhullSetIterator<QhullFacet> QhullFacetSetIterator;
- select_all · function · L43-L43 — QhullFacetSet(const QhullFacetSet &other) : QhullSet<QhullFacet>(other), select_all(other.select_all) {}
- count · function · L62-L67 — countT              count() const;
- contains · function · L63-L63 — bool                contains(const QhullFacet &f) const;
- count · function · L64-L64 — countT              count(const QhullFacet &f) const;
- isSelectAll · function · L65-L65 — bool                isSelectAll() const { return select_all; }
- selectAll · function · L67-L67 — void                selectAll() { select_all= true; }
- selectGood · function · L68-L68 — void                selectGood() { select_all= false; }
- PrintFacetSet · class · L73-L87 — struct PrintFacetSet
- facet_set · function · L83-L84 — PrintIdentifiers(const char *message, const QhullFacetSet *s) : facet_set(s), print_message(message) {}
- print_message · function · L83-L83 — PrintIdentifiers(const char *message, const QhullFacetSet *s) : facet_set(s), print_message(message) {}
- printIdentifiers · function · L85-L85 — PrintIdentifiers    printIdentifiers(const char *message) const { return PrintIdentifiers(message, this); }
