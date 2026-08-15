
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "*" + spell + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
            "max_power": max(mages, key=lambda mage: mage["power"])["power"],
            "min_power": min(mages, key=lambda mage: mage["power"])["power"],
            "avg_power": round(sum(map(lambda mage: mage["power"], mages))
                               / len(mages), 2)
    }


if __name__ == "__main__":
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

    print("Testing artifact sorter ...")
    print(artifact_sorter(artifacts))
    print("Testing mages power filter ...")
    print(power_filter(mages, 60))
    print("Testing spells transformer ...")
    print(spell_transformer(spells))
    print("Testing mages stats ...")
    print(mage_stats(mages))
