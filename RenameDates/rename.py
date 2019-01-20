import pathlib
import sys

path = sys.argv[1]

folder = pathlib.Path(path)
subfolders = [f for f in folder.iterdir() if f.is_dir()]
for f in subfolders:
    extension = f.name[12:]
    year1 = f.name[8:10]
    year2 = f.name[5:7]
    month = f.name[1:3]
    day = f.name[10:12]
    new_name = f"{year1}{year2}_{month}_{day}{extension}"
    target = pathlib.Path(str(path) + "\\" + new_name)
    f.rename(target)
