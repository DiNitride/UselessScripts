import pathlib

# Blacklisted folders to ignore when contructing index
BLACKLIST = [
    ".git"
]
NO_DESC_MESSAGE = "No description provided."

template = """
# UselessScripts
A collections of mildly sometimes useful scripts and tools that are only applicable for my own use probably

## Index

"""

index = ""
uselessFolder = pathlib.Path(".")
folders = [f for f in uselessFolder.iterdir() if f.is_dir()]
for folder in folders:
    if folder.name in BLACKLIST:
        continue
    try:
        with open(f"{folder}/README.md") as f:
            data = f.readlines()
            desc = data[2].replace("#", " ").strip()
            name = data[0].replace("#", " ").strip()
    except FileNotFoundError:
        desc = NO_DESC_MESSAGE
        name = folder
    print(f"{folder}, {name}, {desc}")
    index_entry = f"[{name}]({folder}) - {desc}\n\n"
    template += index_entry

print(template)

with open("README.md", "w") as f:
    f.write(template)
