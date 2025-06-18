# 🖼️ Image Converter: JPG to PNG

# 🖼️ JPG to PNG Converter

A simple Python script to batch convert images from `.jpg` (or other formats) to `.png`.

## 📂 What It Does

* Takes two command-line arguments:

  1. Input folder containing images
  2. Output folder where converted `.png` files will be saved
* Converts all images to PNG format using the [Pillow](https://python-pillow.org/) library
* Automatically creates the output folder if it doesn't exist
* Keeps the original filenames (but with `.png` extension)

## 🛠️ Requirements

* Python 3.x
* [Pillow](https://pypi.org/project/Pillow/)

Install Pillow via pip:

```bash
pip install Pillow
```

## 🚀 Usage

Run the script from the command line:

```bash
python jpg-to-png-converter.py <input_folder> <output_folder>
```

### Example

```bash
python jpg-to-png-converter.py ./images/ ./converted/
```

* `./images/` – Folder with `.jpg` images
* `./converted/` – Destination folder for `.png` images

## 📌 Notes

* Input paths must end with a `/` (on Unix/macOS) or `\\` (on Windows) to avoid file path issues.
* All converted images are saved in `.png` format regardless of their original type.
* Subdirectories are not processed — only files in the specified folder are handled.
