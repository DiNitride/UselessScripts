import sys
import subprocess
import shutil

OUTPUT_DIR = "D:\\DiNitride\\Videos\\YouTube\\Cuts"
MOVE_DIR = "D:\\DiNitride\\Videos\\YouTube\\Raw Cuts"

FILE = sys.argv[1]

minutes = 0
seconds = 0
t = 0

print(f"Clipping file {FILE}")
minutes = int(input("Start time (Minutes): "))
seconds = int(input("Start time (Seconds): "))
t = (minutes * 60) + seconds
rename = input("Rename?: ")

if rename == "":
    rename = FILE

r = subprocess.run(f"ffmpeg -i \"{FILE}\" -vcodec copy -acodec copy -map 0 -ss {t} -c:v copy -c:a copy \"{OUTPUT_DIR}\\{rename}.mp4\"")

if r.returncode == 0:
    shutil.move(FILE, MOVE_DIR)
