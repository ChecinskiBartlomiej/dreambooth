from pathlib import Path
from PIL import Image

cwd        = Path(__file__).resolve().parent
input_dir  = cwd / "data" / "raw"
output_dir = cwd / "data" / "cropped"

def center_crop(img: Image.Image) -> Image.Image:
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top  = (h - side) // 2
    return img.crop((left, top, left + side, top + side))

for path_in in input_dir.iterdir():
    if path_in.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue

    path_out = output_dir / path_in.name

    with Image.open(path_in) as img:
        img_cropped = center_crop(img)
        img_resized = img_cropped.resize((512, 512), Image.LANCZOS)
        img_resized.save(path_out)

    print(f"✔ {path_in.name} → {path_out}")


