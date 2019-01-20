import datetime
import pathlib
import sys

time = datetime.date.today()
try:
    type = sys.argv[1]
except IndexError:
    type = "L"
name = input("Name: ").replace(" ", "_")

pathlib.Path(f"./{time.year}_{time.month}_{time.day}_{type}_{name}").mkdir()
