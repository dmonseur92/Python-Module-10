import functools as ft
import operator as op
from collections.abc import Callable
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return ft.reduce(op.add, spells)
    elif operation == "multiply":
        return ft.reduce(op.mul, spells)
    elif operation == "max":
        return ft.reduce(max, spells)
    elif operation == "min":
        return ft.reduce(min, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")

def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Launch a {element} spell and do {power} damage to {target}!"

def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire_enchant": ft.partial(base_enchantment, 50, "fire"),
        "ice_enchant": ft.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": ft.partial(base_enchantment, 50, "lightning"),
    }

@ft.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable:
    @ft.singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)}"

    return spell

if __name__ == "__main__":
    print("Testing spell reducer...")
    try:
        print(spell_reducer([14, 27, 38, 28, 36, 10], "add"))
        print(spell_reducer([14, 27, 38, 28, 36, 10], "multiply"))
        print(spell_reducer([14, 27, 38, 28, 36, 10], "max"))
        print(spell_reducer([14, 27, 38, 28, 36, 10], "min"))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("\nTesting partial enchanter...")
    try:
        enchantments = partial_enchanter(base_enchantment)
        print(enchantments["fire_enchant"]("Dragon"))
        print(enchantments["ice_enchant"]("Goblin"))
        print(enchantments["lightning_enchant"]("Wizard"))
    except (TypeError, KeyError) as e:
        print(f"Error: {e}")

    print("\nTesting memoized fibonacci...")
    try:
        print(f"Fib(14): {memoized_fibonacci(14)}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    print("\nTesting spell dispatcher...")
    try:
        spell = spell_dispatcher()
        print(spell(50))
        print(spell("fire"))
        print(spell([10, 20, 30]))
        print(spell(3.14))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
