# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 08:55:30 by stmaire         #+#    #+#               #
#  Updated: 2026/03/16 08:43:14 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args: Any, **kwargs: Any) -> tuple | str:
        try:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        except Exception as e:
            return f"cannot cast spells: {e}"

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args, **kwargs) -> int | float | str:
        try:
            result = base_spell(*args, **kwargs)
            return result * multiplier
        except (TypeError, ValueError) as e:
            return (f"Cannot amplify : Invalid args: {e}")

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def valid_cast_spell(*args, **kwargs) -> str:
        try:
            valid = condition(*args, **kwargs)
            if valid is False:
                return "Spell fizzled"
            return spell(*args, **kwargs)
        except Exception as e:
            return f"cannot cast spells: {e}"

    return valid_cast_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_ordered_spells(*args, **kwargs) -> list[Any] | str:
        try:
            return [s(*args, **kwargs) for s in spells]
        except Exception as e:
            return f"cannot cast spells: {e}"

    return cast_ordered_spells


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(target) -> str:
        return f"Fireball hits {target}"

    def heal(target) -> str:
        return f"Heals {target}"

    def feeze(target) -> str:
        return f"Feeze ices {target}"

    combined = spell_combiner(fireball, heal)
    result = (combined("dragon"))
    clean_result = ", ".join(result)
    print(f"Combined spell result: {clean_result}")

    print("\nTesting power amplifier...")

    def damage_spell(target) -> int:
        return 10

    amplified = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell('dragon')}, "
          f"Amplified: {amplified('dragon')}")

    print("\nTesting conditional caster...")

    def is_dragon(target) -> bool:
        if target.lower() != "dragon":
            return False
        return True

    casted_spell = conditional_caster(is_dragon, fireball)
    print(f"{casted_spell('Dragon')}")
    print(f"{casted_spell('Wizard')}")

    print("\nTesting spell_sequence...")
    ordered_spells = spell_sequence([fireball, heal, feeze])
    result = ordered_spells('Dragon')
    clean_result = ", ".join(result)
    print(f"{clean_result}")


if __name__ == "__main__":
    main()
