# 🖼️ PNG to WebP Converter (via in-memory JPEG)

This Python tool converts all `.png` images in a folder to `.webp` format, using an **in-memory JPEG** as an intermediate step. It leverages the `Pillow` library and avoids saving intermediate `.jpg` files to disk.

---

## 📦 Features

- Convert `.png` to `.webp` with JPEG-quality compression step in memory.
- No temporary `.jpg` files created.
- Adjustable JPEG and WebP compression quality.
- Lightweight and simple to use.
- Output files saved in a separate `output/` directory.

---

## 📁 Folder Structure

```
image-converter/
├── convert.py          # Main conversion script
├── images/             # Place your .png files here
│   ├── example1.png
│   └── example2.png
├── output/             # Converted .webp files will be saved here
└── readme.md
```

---

## 🚀 Getting Started

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/image-converter.git
cd image-converter
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, manually install Pillow:

```bash
pip install pillow
```

### 4. Add Your PNG Images

Place all your `.png` images inside the `images/` folder.

### 5. Run the Script

```bash
python convert.py
```

Converted `.webp` files will be saved to the `output/` folder.

---

## ⚙️ Configuration

You can adjust compression quality by modifying this part in `convert.py`:

```python
convert_png_to_webp_via_jpeg_memory(
    input_folder="images",
    output_folder="output",
    jpg_quality=70,      # JPEG compression (in-memory)
    webp_quality=60      # Final WebP compression
)
```

### ✅ Recommended Quality Values

- `jpg_quality`: 60–80
- `webp_quality`: 50–80

---

