# resizer_tool
# Image Resizer Tool (Python + Pillow)

## 📌 Task Objective
Resize and convert images in **batch** using Python and Pillow.

---

## 🛠️ Requirements
- Python 3.9+ installed
- Install Pillow library:
  ```bash
  pip install pillow
  ```

---

## 📂 Project Structure
```
image_resizer_task/
 ┣ 📂 input_images/    # Put your input images here (jpg, png, webp, bmp, tiff)
 ┣ 📂 output_images/   # Resized images will be saved here
 ┗ 📄 resize_images.py # Script to run
```

---

## ▶️ How to Run

1. Place all your input images inside the `input_images/` folder.

2. Open terminal in this project folder and run:
   ```bash
   python resize_images.py
   ```

3. Resized images will appear in the `output_images/` folder.

---

## ⚙️ Customization
Inside `resize_images.py`, you can change:
- `width=800, height=800` → output dimensions
- `fit="contain"` → resizing mode (`contain | cover | stretch`)
- `fmt="keep"` → output format (`keep | jpg | png | webp | bmp | tiff`)

---

## ✅ Example
Input: `dog.jpg` (1920x1080) in `input_images/`  
Output: `dog_resized.jpg` (800x450) in `output_images/`

---

## Author
Priyam Yadav
