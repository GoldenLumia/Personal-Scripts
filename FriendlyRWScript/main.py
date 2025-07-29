import os
import shutil
import zipfile
import pytz
from datetime import datetime

# 1. Locate the folder containing the two subdirectories
source_dirs = [
    r"C:\PLACEHOLDER\",
    r"C:\PLACEHOLDER\"
]

# 2. Create a copy of those subdirectories to another root directory
destination_root = r"H:\Data"
os.makedirs(destination_root, exist_ok=True)

for src in source_dirs:
    dst = os.path.join(destination_root, os.path.basename(src))
    if os.path.exists(dst):
        shutil.rmtree(dst)  # remove if already exists
    shutil.copytree(src, dst)

# 3. Search for About.xml in the copied subdirectories and modify
for root, dirs, files in os.walk(destination_root):
    if "About.xml" in files:
        about_path = os.path.join(root, "About.xml")
        with open(about_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(about_path, "w", encoding="utf-8") as f:
            for line in lines:
                if "<steamAppId>" not in line:
                    f.write(line)

# Make sure the root folder exists before zipping
zip_root = r"H:\testing"
os.makedirs(zip_root, exist_ok=True)

# 4. Create a timestamp for the zip filename in Eastern Time
eastern = pytz.timezone("US/Eastern")
timestamp = datetime.now(eastern).strftime("%Y%m%d_%H%M%S")
zip_name = f"RimWorldDLC_{timestamp}.zip"
zip_path = os.path.join(zip_root, zip_name)

# 5. Zip the entire directory, avoiding including any .zip files inside
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(destination_root):
        for file in files:
            if file.lower().endswith(".zip"):
                continue  # skip any .zip files inside
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(destination_root))
            zipf.write(file_path, arcname)

print("Done! Copied, modified, and zipped to:", zip_path)
