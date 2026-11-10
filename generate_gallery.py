import json
from pathlib import Path

# Folder containing all portfolio photographs
image_folder = Path("/var/www/html/weiserchoice/images/photos")

# Supported image formats
image_types = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

gallery = []

for photo in sorted(image_folder.iterdir()):
    if photo.is_file() and photo.suffix.lower() in image_types:
        gallery.append(f"images/photos/{photo.name}")

# Create the gallery data file
output = Path("/var/www/html/weiserchoice/gallery-data.js")

output.write_text(
    "const galleryPhotos = " + json.dumps(gallery, indent=4) + ";\n",
    encoding="utf-8"
)

print(f"Success! Found {len(gallery)} photographs.")
