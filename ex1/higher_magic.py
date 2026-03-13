from typing import Callable, Any

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine deux sorts pour qu'ils soient lancés simultanément. [cite: 203]
    Retourne un tuple contenant les résultats des deux sorts. [cite: 205]
    """
    def combined_spell(*args: Any, **kwargs: Any) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplifie la puissance d'un sort de base par un multiplicateur. [cite: 208]
    """
    def amplified_spell(*args: Any, **kwargs: Any) -> int | float:
        return base_spell(*args, **kwargs) * multiplier
    
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Lance un sort uniquement si une condition magique est remplie. [cite: 212]
    """
    def cast_if_ready(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"  
    
    return cast_if_ready


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Crée une séquence de sorts lancés les uns après les autres. [cite: 216]
    Retourne une liste de tous les résultats. [cite: 217, 219]
    """
    def sequence_executor(*args: Any, **kwargs: Any) -> list:
        return [s(*args, **kwargs) for s in spells]
    
    return sequence_executor


def main() -> None:
    fireball = lambda target: f"Fireball hits {target}"
    heal = lambda target: f"Heals {target}"
    damage_spell = lambda _: 10
    is_dragon = lambda target: target.lower() == "dragon"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}") [cite: 223]

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(damage_spell, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon')}") [cite: 225]

    print("\nTesting conditional caster...")
    dragon_slayer = conditional_caster(is_dragon, fireball)
    print(f"Targeting Dragon: {dragon_slayer('Dragon')}")
    print(f"Targeting Goblin: {dragon_slayer('Goblin')}")

    print("\nTesting spell sequence...")
    barrage = spell_sequence([fireball, heal])
    print(f"Sequence results: {barrage('Warrior')}")

if __name__ == "__main__":
    main()