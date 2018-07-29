import pathlib
import json

MODS_DIR = "/home/steam/starbound_server/steamapps/workshop/content/211820"
CONFIG_FILE = "/home/steam/starbound_server/linux/sbinit.config"
TEMPLATE = "../steamapps/workshop/content/211820/{}/"
ASSET_DIR_TEMPLATE = ["../assets/", "../mods/"]

with open(CONFIG_FILE) as f:
    print("Loading config file")
    config = json.load(f)

config["assetDirectories"] = ASSET_DIR_TEMPLATE
mods_folder = pathlib.Path(MODS_DIR)
mods = [f for f in mods_folder.iterdir() if f.is_dir()]
print(f"Loaded {len(mods)} mods")
for mod in mods:
    config["assetDirectories"].append(TEMPLATE.format(mod.name))
    print(TEMPLATE.format(mod.name))

print(config)

with open(CONFIG_FILE, "w") as f:
    f.write(json.dumps(config, indent=2, separators=(',', ':')))
