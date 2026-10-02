# src/slic3r/Config/Version.hpp

- Version · class · L17-L33 — struct Version
- is_slic3r_supported · function · L30-L30 — bool 		is_slic3r_supported(const Semver &slicer_version) const;
- is_current_slic3r_supported · function · L31-L31 — bool 		is_current_slic3r_supported() const;
- is_current_slic3r_downgrade · function · L32-L32 — bool 		is_current_slic3r_downgrade() const;
- Index · class · L54-L89 — class Index
- const_iterator · type · L57-L57 — typedef std::vector<Version>::const_iterator const_iterator;
- load · function · L60-L60 — size_t						load(const boost::filesystem::path &path);
- vendor · function · L62-L62 — const std::string&			vendor() const { return m_vendor; }
- version · function · L65-L65 — Semver						version() const;
- begin · function · L67-L67 — const_iterator				begin()   const { return m_configs.begin(); }
- end · function · L68-L68 — const_iterator				end()     const { return m_configs.end(); }
- find · function · L69-L69 — const_iterator 				find(const Semver &ver) const;
- configs · function · L70-L70 — const std::vector<Version>& configs() const { return m_configs; }
- recommended · function · L74-L74 — const_iterator				recommended() const;
- recommended · function · L76-L76 — const_iterator				recommended(const Semver &slic3r_version) const;
- path · function · L79-L79 — const boost::filesystem::path& path() const { return m_path; }
- load_db · function · L83-L83 — static std::vector<Index>	load_db();
