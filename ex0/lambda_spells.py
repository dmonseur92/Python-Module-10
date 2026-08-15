def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact:artifact["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))

if  __name__ == "__main__":
    artifacts = [{'name': 'Earth Shield', 'power': 104, 'type': 'relic'},
                 {'name': 'Ice Wand', 'power': 78, 'type': 'relic'},
                 {'name': 'Shadow Blade', 'power': 110, 'type': 'accessory'},
                {'name': 'Lightning Rod', 'power': 120, 'type': 'armor'}]
    mages = [{'name': 'Jordan', 'power': 87, 'element': 'lightning'},
             {'name': 'Storm', 'power': 86, 'element': 'fire'},
             {'name': 'Storm', 'power': 59, 'element': 'ice'},
             {'name': 'Alex', 'power': 61, 'element': 'lightning'},
             {'name': 'Phoenix', 'power': 52, 'element': 'lightning'}]
    spells = ['flash', 'tsunami', 'heal', 'earthquake']

    print(artifact_sorter(artifacts))
    print(power_filter(mages, 100))


