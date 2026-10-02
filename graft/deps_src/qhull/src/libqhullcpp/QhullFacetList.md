# deps_src/qhull/src/libqhullcpp/QhullFacetList.h

- QhullFacetListIterator · type · L33-L33 — typedef QhullLinkedListIterator<QhullFacet> QhullFacetListIterator;
- select_all · function · L45-L45 — QhullFacetList(QhullFacet b, QhullFacet e) : QhullLinkedList<QhullFacet>(b, e), select_all(false) {}
- end · function · L47-L47 — QhullFacetList(const QhullFacetList &other) : QhullLinkedList<QhullFacet>(*other.begin(), *other.end()), select_all(other.select_all) {}
- QhullFacetList · function · L47-L47 — QhullFacetList(const QhullFacetList &other) : QhullLinkedList<QhullFacet>(*other.begin(), *other.end()), select_all(other.select_all) {}
- select_all · function · L47-L47 — QhullFacetList(const QhullFacetList &other) : QhullLinkedList<QhullFacet>(*other.begin(), *other.end()), select_all(other.select_all) {}
- count · function · L67-L71 — countT              count() const;
- contains · function · L68-L68 — bool                contains(const QhullFacet &f) const;
- count · function · L69-L69 — countT              count(const QhullFacet &f) const;
- isSelectAll · function · L70-L70 — bool                isSelectAll() const { return select_all; }
- qh · function · L71-L71 — QhullQh *           qh() const { return first().qh(); }
- selectAll · function · L72-L72 — void                selectAll() { select_all= true; }
- selectGood · function · L73-L73 — void                selectGood() { select_all= false; }
- PrintFacetList · class · L77-L87 — struct PrintFacetList
- facet_list · function · L86-L86 — PrintFacets(const QhullFacetList &fl) : facet_list(&fl) {}
- printFacets · function · L88-L88 — PrintFacets         printFacets() const { return PrintFacets(*this); }
- PrintVertices · class · L90-L101 — struct PrintVertices
