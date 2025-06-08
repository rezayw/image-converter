import os
from PIL import Image
from io import BytesIO

def convert_png_to_webp_via_jpeg_memory(input_folder, output_folder, jpg_quality=70, webp_quality=60):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            base_name = os.path.splitext(filename)[0]
            webp_path = os.path.join(output_folder, base_name + ".webp")

            # Open PNG and convert to RGB (remove alpha channel)
            with Image.open(input_path).convert("RGB") as img:
                # Save JPEG to memory buffer (not disk)
                jpeg_buffer = BytesIO()
                img.save(jpeg_buffer, format="JPEG", quality=jpg_quality, optimize=True)
                jpeg_buffer.seek(0)

                # Load JPEG from memory and convert to WebP
                with Image.open(jpeg_buffer) as jpeg_img:
                    jpeg_img.save(webp_path, format="WEBP", quality=webp_quality, method=6)
                    print(f"✔️ {filename} → WebP via JPEG memory (saved to {webp_path})")

# Jalankan fungsi
convert_png_to_webp_via_jpeg_memory(
    input_folder="images",
    output_folder="output",
    jpg_quality=50,     # Kompresi JPEG in-memory
    webp_quality=50     # Kompresi hasil WebP
)
