import pathlib
import shutil

# Move stuff from here
SD_FOLDER = "D:\\DCIM\\100CANON"
# To here
IMPORT_BIN = "C:\\Users\\DiNitride\\Pictures\\Camera SD"

SDCardFolder = pathlib.Path(SD_FOLDER)
files = [f for f in SDCardFolder.iterdir() if f.is_file()]
for file in files:
    shutil.move(str(file), IMPORT_BIN)
    print(f"Moved {file}")
