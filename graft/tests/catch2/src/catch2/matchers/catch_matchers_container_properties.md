# tests/catch2/src/catch2/matchers/catch_matchers_container_properties.hpp

- IsEmptyMatcher · class · L18-L31 — class IsEmptyMatcher final : public MatcherGenericBase
- match · function · L20-L28 — template <typename RangeLike>
- describe · function · L30-L30 — std::string describe() const override;
- HasSizeMatcher · class · L33-L51 — class HasSizeMatcher final : public MatcherGenericBase
- HasSizeMatcher · function · L36-L38 — explicit HasSizeMatcher(std::size_t target_size):
- match · function · L40-L48 — template <typename RangeLike>
- describe · function · L50-L50 — std::string describe() const override;
- SizeMatchesMatcher · class · L53-L74 — template <typename Matcher>
- SizeMatchesMatcher · function · L57-L59 — explicit SizeMatchesMatcher(Matcher m):
- match · function · L61-L69 — template <typename RangeLike>
- describe · function · L71-L73 — std::string describe() const override
- IsEmpty · function · L78-L78 — IsEmptyMatcher IsEmpty();
- SizeIs · function · L80-L80 — HasSizeMatcher SizeIs(std::size_t sz);
- SizeIs · function · L81-L85 — template <typename Matcher>
