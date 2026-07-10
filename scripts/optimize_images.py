from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]

SOURCES = [
    ("assets/hero/hero.jpg", [("hero", None), ("hero-mobile", 900)]),
    ("assets/about/about.jpg", [("about", None)]),
    ("assets/classes/technique.jpg", [("technique", None)]),
    ("assets/classes/conditioning.jpg", [("conditioning", None)]),
    ("assets/classes/mindset.jpg", [("mindset", None)]),
    ("assets/classes/sparring.jpg", [("sparring", None)]),
]


def resized(image, target_width):
    if target_width is None or image.width <= target_width:
        return image.copy()

    ratio = target_width / image.width
    target_height = round(image.height * ratio)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


def save_variants(source, variants):
    source_path = ROOT / source
    image = Image.open(source_path).convert("RGB")

    for name, target_width in variants:
        output = resized(image, target_width)
        base_path = source_path.with_name(name)
        output.save(base_path.with_suffix(".webp"), "WEBP", quality=78, method=6)
        output.save(base_path.with_suffix(".avif"), "AVIF", quality=58, speed=6)
        print(f"{base_path.with_suffix('.webp').relative_to(ROOT)} {output.size}")
        print(f"{base_path.with_suffix('.avif').relative_to(ROOT)} {output.size}")


for source, variants in SOURCES:
    save_variants(source, variants)
