# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 16:25:56 by stmaire         #+#    #+#               #
#  Updated: 2026/03/16 16:08:17 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable, Any, Dict
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: Dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        return 0
    if not spells:
        return 0

    try:
        return (functools.reduce(operations[operation], spells))
    except Exception:
        return 0


def base_enchantment(power: int, element: str, target: str) -> str:
    if not isinstance(power, int) or power < 0:
        return ("Power must be a positive integer")
    if not isinstance(element, str) or not isinstance(target, str):
        return ("Invalid element or target")
    return (f"{element} {target} with {power}")


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    enchanters: dict[str, Callable[[str], str]] = {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment,
            50,
            "lightning"
            )
    }
    return (enchanters)


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(data: Any) -> str:
        return (f"Spell cannot be created: {data} is not a valid data."
                f"(Data must be int, str or list)")

    @dispatcher.register(int)
    def _(damage_spell: int) -> str:
        return (f"Suffer {damage_spell} points of damage")

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return (f"Enchantment is {enchantment}")

    @dispatcher.register(list)
    def _(multi_cast: list) -> str:
        return (f"'Cast {len(multi_cast)} spells'")

    return dispatcher


def main() -> None:
    print("\nTesting spell reducer...")

    spells = [10, 20, 30, 40]

    addition = spell_reducer(spells, "add")
    print(f"Sum: {addition}")
    multiplication = spell_reducer(spells, "multiply")
    print(f"Product: {multiplication}")
    maximum = spell_reducer(spells, "max")
    print(f"Max: {maximum}")

    print("\nTesting partial_enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire_enchant"]("dragon"))
    print(enchanters["lightning_enchant"]("wizard"))

    print("\nTesting memoized fibonacci")
    result = memoized_fibonacci(10)
    print(f"Fib(10) = {result}")
    result = memoized_fibonacci(35)
    print(f"Fib(35) = {result}")

    print("\nTesting spell dispatcher")
    cast = spell_dispatcher()
    print(f"Cast: damage spell = 10 : '{cast(10)}'")
    print(f"Cast: enchantment = 'Petrification': '{cast('Petrification')}'")
    print(f"Multicast: ('Petrification', 'Levitation'): "
          f"{cast(['Petrification', 'Levitation'])}")
    print(f"Testing another value: float 4.2: {cast(4.2)}")


if __name__ == "__main__":
    main()
