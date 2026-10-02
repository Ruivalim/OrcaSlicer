# deps_src/hidapi/include/hidapi.h

- hid_device · type · L46-L46 — typedef struct hid_device_ hid_device; /**< opaque hidapi structure */
- hid_device_info · class · L49-L83 — struct hid_device_info
- hid_init · function · L100-L100 — int HID_API_EXPORT HID_API_CALL hid_init(void);
- hid_exit · function · L113-L113 — int HID_API_EXPORT HID_API_CALL hid_exit(void);
- hid_free_enumeration · function · L146-L146 — void  HID_API_EXPORT HID_API_CALL hid_free_enumeration(struct hid_device_info *devs);
- hid_write · function · L207-L207 — int  HID_API_EXPORT HID_API_CALL hid_write(hid_device *dev, const unsigned char *data, size_t length);
- hid_read_timeout · function · L228-L228 — int HID_API_EXPORT HID_API_CALL hid_read_timeout(hid_device *dev, unsigned char *data, size_t length, int milliseconds);
- hid_read · function · L248-L248 — int  HID_API_EXPORT HID_API_CALL hid_read(hid_device *dev, unsigned char *data, size_t length);
- hid_set_nonblocking · function · L268-L268 — int  HID_API_EXPORT HID_API_CALL hid_set_nonblocking(hid_device *dev, int nonblock);
- hid_send_feature_report · function · L296-L296 — int HID_API_EXPORT HID_API_CALL hid_send_feature_report(hid_device *dev, const unsigned char *data, size_t length);
- hid_get_feature_report · function · L321-L321 — int HID_API_EXPORT HID_API_CALL hid_get_feature_report(hid_device *dev, unsigned char *data, size_t length);
- hid_close · function · L328-L328 — void HID_API_EXPORT HID_API_CALL hid_close(hid_device *dev);
- hid_get_manufacturer_string · function · L340-L340 — int HID_API_EXPORT_CALL hid_get_manufacturer_string(hid_device *dev, wchar_t *string, size_t maxlen);
- hid_get_product_string · function · L352-L352 — int HID_API_EXPORT_CALL hid_get_product_string(hid_device *dev, wchar_t *string, size_t maxlen);
- hid_get_serial_number_string · function · L364-L364 — int HID_API_EXPORT_CALL hid_get_serial_number_string(hid_device *dev, wchar_t *string, size_t maxlen);
- hid_get_indexed_string · function · L377-L377 — int HID_API_EXPORT_CALL hid_get_indexed_string(hid_device *dev, int string_index, wchar_t *string, size_t maxlen);
