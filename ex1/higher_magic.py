from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball burns {target} for {power} HP"

def lightning_strike(target: str, power: int) -> str:
    return f"Lightning strike shocks {target} for {power * 2} HP"

def heal(target: str, power: int) -> str:
    return f"Heal {target} for {power} HP"

def is_healer_not_afk(target: str, power: int) -> bool:
    if target == 'Wizard' or target == 'Knight' and power > 9:
        return True
    else:
        return False

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def verify(target: str, power: int) -> str:
        if condition (target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return verify

def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_spells(target, power):
        return list(map(lambda spell: spell(target, power), spells))
    return cast_spells



if __name__ == "__main__":
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combo = spell_combiner(fireball, lightning_strike)
    print(combo("Goblin", 16))

    boom_boom_dmg = power_amplifier(fireball, 5)
    print(boom_boom_dmg("Dragon", 10))

    heal_me_plz = conditional_caster(is_healer_not_afk, heal)
    print(heal_me_plz("Knight", 2))

    mastery_display = spell_sequence([fireball, lightning_strike, heal])
    print(mastery_display("Goblin", 500))
