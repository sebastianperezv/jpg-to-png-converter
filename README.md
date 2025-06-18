# 🖼️ Image Converter: JPG to PNG

This Python script converts all images in a specified input folder into `.png` format and saves them into an output folder.

## 📂 What It Does

* Takes two command-line arguments: the input folder path and the output folder path.
* Reads all images in the input folder (e.g., `.jpg`, `.jpeg`).
* Converts each image to `.png`.
* Saves them into the specified output folder.
* Automatically creates the output folder if it doesn't exist.

## 🛠️ Requirements

* Python 3.x
* [Pillow](https://python-pillow.org/) (Python Imaging Library fork)

Install Pillow if you don’t have it:

```bash
pip install Pillow
```

## 🚀 Usage

From the command line, run:

```bash
python convert.py <input_folder> <output_folder>
```

### Example

```bash
python convert.py ./images/ ./converted/
```

* `./images/`: Folder containing source images.
* `./converted/`: Target folder for `.png` files.

## 📌 Notes

* The script assumes images are directly in the input folder (no subdirectories).
* Converted images keep the original filename (but with `.png` extension).
* Make sure to include a trailing slash (`/`) in the folder paths if you're on Unix/macOS. On Windows, you might use `\\` or raw strings.

---

Let me know if you want to include:

* Logging instead of `print()`
* Recursively processing subfolders
* Example images or screenshots
* A license file (like MIT)

