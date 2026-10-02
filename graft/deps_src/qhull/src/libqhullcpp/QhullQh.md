# deps_src/qhull/src/libqhullcpp/QhullQh.h

- qh_fprintf · function · L69-L69 — friend void         ::qh_fprintf(qhT *qh, FILE *fp, int msgcode, const char *fmt, ... );
- factorEpsilon · function · L84-L84 — double              factorEpsilon() const { return factor_epsilon; }
- setFactorEpsilon · function · L85-L85 — void                setFactorEpsilon(double a) { factor_epsilon= a; }
- disableOutputStream · function · L86-L86 — void                disableOutputStream() { use_output_stream= false; }
- enableOutputStream · function · L87-L87 — void                enableOutputStream() { use_output_stream= true; }
- appendQhullMessage · function · L90-L90 — void                appendQhullMessage(const std::string &s);
- clearQhullMessage · function · L91-L91 — void                clearQhullMessage();
- qhullMessage · function · L92-L92 — std::string         qhullMessage() const;
- hasOutputStream · function · L93-L93 — bool                hasOutputStream() const { return use_output_stream; }
- hasQhullMessage · function · L94-L102 — bool                hasQhullMessage() const;
- maybeThrowQhullMessage · function · L96-L96 — void                maybeThrowQhullMessage(int exitCode, int noThrow) throw();
- qhullStatus · function · L97-L97 — int                 qhullStatus() const;
- angleEpsilon · function · L102-L102 — double              angleEpsilon() const { return this->ANGLEround*factor_epsilon; } //!< Epsilon for hyperplane angle equality
- checkAndFreeQhullMemory · function · L103-L103 — void                checkAndFreeQhullMemory();
- distanceEpsilon · function · L104-L104 — double              distanceEpsilon() const { return this->DISTround*factor_epsilon; } //!< Epsilon for distance to hyperplane
