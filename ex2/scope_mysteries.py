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
    def enchanting(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanting


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("Testing mage counter...")
    counter1 = mage_counter()
    counter2 = mage_counter()
    print(f"counter1: {counter1()}")
    print(f"counter1: {counter1()}")
    print(f"counter1: {counter1()}")
    print(f"counter2: {counter2()}")
    print()

    print("Testing spell accumulator...")
    kamehameha = spell_accumulator(10)
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(100)}")
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(1000)}")
    print(f"GoTrunks is powering up: kamehameha value = {kamehameha(10000)}")
    print()

    print("Testing enchantment factory...")
    dream = enchantment_factory("Flaming")
    print(dream("Sword"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    print(vault["store"]("secret", "42"))
    print(vault["recall"]("secret"))
    print(vault["recall"]("age"))
