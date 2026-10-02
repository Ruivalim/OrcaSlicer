# src/libslic3r/GCode/Thumbnails.hpp

- ThumbnailError · type · L17-L17 — enum class ThumbnailError : int { InvalidVal, OutOfRange, InvalidExt };
- CompressedImageBuffer · class · L24-L30 — struct CompressedImageBuffer
- tag · function · L29-L29 — virtual std::string_view tag() const = 0;
- get_hex · function · L32-L32 — std::string get_hex(const unsigned int input);
- rjust · function · L33-L33 — std::string rjust(std::string input, unsigned int width, char fill_char);
- compress_thumbnail · function · L34-L34 — std::unique_ptr<CompressedImageBuffer> compress_thumbnail(const ThumbnailData &data, GCodeThumbnailsFormat format);
- get_error_string · function · L35-L35 — std::string get_error_string(const ThumbnailErrors& errors);
- GCodeThumbnailDefinitionsList · type · L38-L38 — typedef std::vector<std::pair<GCodeThumbnailsFormat, Vec2d>> GCodeThumbnailDefinitionsList;
- make_and_check_thumbnail_list · function · L40-L40 — std::pair<GCodeThumbnailDefinitionsList, ThumbnailErrors> make_and_check_thumbnail_list(const std::string& thumbnails_string, const std::string_view def_ext = "PNG"sv);
- make_and_check_thumbnail_list · function · L41-L41 — std::pair<GCodeThumbnailDefinitionsList, ThumbnailErrors> make_and_check_thumbnail_list(const ConfigBase &config);
- export_thumbnails_to_file · function · L44-L105 — template<typename WriteToOutput, typename ThrowIfCanceledCallback>
