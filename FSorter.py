import shutil
from pathlib import Path

# Get paths
DOWNLOADS_FOLDER = Path.home() / "Downloads"
SORTED_FOLDER = Path.home() / "Desktop" / "Sorted Files"

# Create the folder if it doesn't exist
if not SORTED_FOLDER.exists():
    SORTED_FOLDER.mkdir()

# Iterate through files in Downloads
for file in DOWNLOADS_FOLDER.iterdir():
    if file.is_file():
        # Get the file extension (without dot)
        f_extension = file.suffix[1:].capitalize()  

        if f_extension == "":
            f_extension = "no_extension"

        # Destination folder on Desktop
        dest_folder = SORTED_FOLDER / f_extension

        # Create the folder if it doesn't exist
        if not dest_folder.exists():
            dest_folder.mkdir()

        # Move file
        shutil.move(str(file), str(dest_folder / file.name))

print("Files sorted into: ", SORTED_FOLDER)