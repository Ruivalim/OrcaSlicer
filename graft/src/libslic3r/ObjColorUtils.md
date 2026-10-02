# src/libslic3r/ObjColorUtils.hpp

- QuantKMeans · class · L7-L262 — class QuantKMeans
- QuantKMeans · function · L13-L13 — QuantKMeans(int alpha_thres = 10) : m_alpha_thres(alpha_thres) {}
- apply · function · L14-L22 — void apply(cv::Mat &ori_image, cv::Mat &new_image, int num_cluster, int color_space)
- apply_aplha · function · L23-L35 — void apply_aplha(cv::Mat &ori_image, cv::Mat &new_image, int num_cluster, int color_space)
- apply · function · L36-L46 — void apply(cv::Mat &flatten_image, int num_cluster, int color_space)
- apply · function · L47-L58 — void apply(const std::vector<std::array<float, 4>> &ori_colors,
- apply · function · L59-L116 — void apply(const cv::Mat &                    flatten_image8UC3,
- more_than_request · function · L118-L130 — bool more_than_request(const cv::Mat &image8UC3, int target_num)
- compute_num_colors · function · L132-L142 — int compute_num_colors(const cv::Mat &image8UC3)
- is_in · function · L144-L149 — bool is_in(const cv::Vec3b &cur_color, const std::vector<cv::Vec3b> &uniqueImage)
- repeat_center · function · L151-L169 — bool repeat_center(int cur_cluster, const cv::Mat &centers32FC3, int color_space)
- replace_centers · function · L171-L180 — void replace_centers(cv::Mat &ori_image, cv::Mat &new_image)
- repalce_centers_aplha · function · L181-L198 — void repalce_centers_aplha(cv::Mat &ori_image, cv::Mat &new_image)
- convert_color_space · function · L200-L218 — void convert_color_space(const cv::Mat &ori_image, cv::Mat &image, int color_space, bool reverse = false)
- flatten · function · L220-L231 — cv::Mat flatten(cv::Mat &image)
- flatten_alpha · function · L232-L250 — cv::Mat flatten_alpha(cv::Mat &image)
- flatten_vector · function · L251-L261 — cv::Mat flatten_vector(const std::vector<std::array<float, 4>> &ori_colors)
- obj_color_deal_algo · function · L264-L268 — bool obj_color_deal_algo(std::vector<Slic3r::RGBA> &input_colors,
