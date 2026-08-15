from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


if __name__ == "__main__":
    values = [8, 19, 6]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combo = spell_combiner(fireball, heal)
    print(combo("Goblin", 16))
