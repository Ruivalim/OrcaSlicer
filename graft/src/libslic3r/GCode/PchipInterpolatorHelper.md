# src/libslic3r/GCode/PchipInterpolatorHelper.hpp

- PchipInterpolatorHelper · class · L15-L74 — class PchipInterpolatorHelper
- PchipInterpolatorHelper · function · L20-L20 — PchipInterpolatorHelper() = default;
- PchipInterpolatorHelper · function · L27-L27 — PchipInterpolatorHelper(const std::vector<double>& x, const std::vector<double>& y);
- setData · function · L35-L35 — void setData(const std::vector<double>& x, const std::vector<double>& y);
- interpolate · function · L42-L42 — double interpolate(double xi) const;
- computePCHIP · function · L54-L54 — void computePCHIP();
- sortData · function · L59-L59 — void sortData();
- h · function · L66-L66 — double h(int i) const { return x_[i+1] - x_[i]; }
- delta · function · L73-L73 — double delta(int i) const { return (y_[i+1] - y_[i]) / h(i); }
