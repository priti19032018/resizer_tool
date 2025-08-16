import os
from pathlib import Path
from PIL import Image, ImageOps

# Supported image extensions
EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff'}

def resize_images(input_folder, output_folder, width=800, height=800, fit="contain", fmt="keep"):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    for file in input_folder.iterdir():
        if file.is_file() and file.suffix.lower() in EXTS:
            try:
                with Image.open(file) as img:
                    # Correct orientation from EXIF
                    img = ImageOps.exif_transpose(img)

                    # Decide output format
                    out_fmt = fmt if fmt != "keep" else file.suffix.lstrip(".")
                    out_name = f"{file.stem}_resized.{out_fmt}"
                    out_path = output_folder / out_name

                    # Resize strategy
                    if fit == "contain":
                        img_copy = img.copy()
                        img_copy.thumbnail((width, height), Image.Resampling.LANCZOS)
                        out_img = img_copy
                    elif fit == "cover":
                        out_img = ImageOps.fit(img, (width, height), method=Image.Resampling.LANCZOS)
                    else:  # stretch
                        out_img = img.resize((width, height), Image.Resampling.LANCZOS)

                    # Convert RGBA → RGB for JPG
                    if out_fmt in {"jpg", "jpeg"} and out_img.mode in ("RGBA", "P"):
                        out_img = out_img.convert("RGB")

                    # Save
                    out_img.save(out_path)
                    print(f"✅ Saved: {out_path}")

            except Exception as e:
                print(f"❌ Failed on {file}: {e}")

if __name__ == "__main__":
    resize_images(
        input_folder="input_images",
        output_folder="output_images",
        width=800,
        height=800,
        fit="contain",   # options: contain | cover | stretch
        fmt="keep"       # options: keep | jpg | png | webp | bmp | tiff
    )
