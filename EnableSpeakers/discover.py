import soco

for zone in soco.discover():
    print(f"Zone: {zone.player_name}, IP: {zone}, Volume: {zone.volume}")
