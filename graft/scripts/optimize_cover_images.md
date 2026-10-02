# scripts/optimize_cover_images.py

- get_file_size · function · L23-L25 — def get_file_size(path)
- format_size · function · L28-L34 — def format_size(size_bytes)
- check_pngquant_available · function · L37-L39 — def check_pngquant_available()
- optimize_png_with_pngquant · function · L42-L65 — def optimize_png_with_pngquant(img_path, quality_range="65-80")
- optimize_png_pillow · function · L68-L89 — def optimize_png_pillow(img, output_path, has_transparency=True)
- get_image_bbox · function · L92-L121 — def get_image_bbox(img)
- calculate_margins · function · L124-L159 — def calculate_margins(bbox, img_size)
- adjust_image_margins · function · L162-L365 — def adjust_image_margins(img_path, target_content_ratio=0.84, dry_run=False, use_pngquant=False, quality_range="65-80", max_size=None)
- find_and_process_cover_images · function · L368-L438 — def find_and_process_cover_images(base_path, target_ratio=0.84, dry_run=False, use_pngquant=False, quality_range="65-80", max_size=None)
- main · function · L441-L578 — def main()
