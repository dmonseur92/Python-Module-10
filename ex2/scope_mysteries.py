from collections.abc import Callable

def mage_counter() -> Callable:
    counter = 0
    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter
    return increment

def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def power_up(new_power: int) -> int:
        nonlocal total_power
        total_power += new_power
        return total_power
    return power_up

def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanting(item_name: str):
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"
    return enchanting


if __name__ == "__main__":

    enchantment_types = ['Flaming', 'Flowing', 'Dark']
    items_to_enchant = ['Armor', 'Sword', 'Cloak', 'Shield']

    print("Testing mage counter...")
    counter1 = mage_counter()
    counter2 = mage_counter()
    print(f"counter1: {counter1()}")
    print(f"counter1: {counter1()}")
    print(f"counter1: {counter1()}")
    print(f"counter2: {counter2()}")

    print("Testing spell accumulator...")
    kamehameha = spell_accumulator(10)
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(100)}")
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(1000)}")
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(10000)}")

    dream = enchantment_factory("Flaming")
    print(dream("Sword"))
