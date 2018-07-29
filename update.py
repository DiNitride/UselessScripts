import pathlib

# Blacklisted folders to ignore when contructing index
BLACKLIST = [
    ".git"
]
NO_DESC_MESSAGE = "No description provided."

template = """
# UselessScripts
A collections of mildly sometimes useful scripts and tools that are only applicable for my own use probably

## Structure
Each script/topic goes inside it's own folder with a README.md
Line 1 of the README should be a H1 title of the script/topic
Line 3 of the README should be a H2 short description

## Index

"""

index = ""
print("Loading folders")
uselessFolder = pathlib.Path(".")
folders = [f for f in uselessFolder.iterdir() if f.is_dir()]
for folder in folders:
    if folder.name in BLACKLIST:
        continue
    print(f"Collecting data for folder {folder}")
    try:
        with open(f"{folder}/README.md") as f:
            data = f.readlines()
            desc = data[2].replace("#", " ").strip()
            name = data[0].replace("#", " ").strip()
    except FileNotFoundError:
        desc = NO_DESC_MESSAGE
        name = folder
    index_entry = f"[{name}]({folder}) - {desc}\n\n"
    template += index_entry

with open("README.md", "w") as f:
    f.write(template)

print("Updated README.md index!")
input("Press enter to continue. . .")
