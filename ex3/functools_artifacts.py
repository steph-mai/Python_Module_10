import functools
import operator
from typing import Callable, Any

def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        return 0
    return functools.reduce(ops[operation], spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")
    lightning = functools.partial(base_enchantment, power=50, element="lightning")
    
    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatcher(spell_input: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"Cast damage spell: {damage} points"

    @dispatcher.register(str)
    def _(name: str) -> str:
        return f"Cast enchantment: {name}"

    @dispatcher.register(list)
    def _(multi_spells: list) -> str:
        return f"Multi-casting {len(multi_spells)} spells"

    return dispatcher

def main() -> None:
    powers = [10, 20, 30, 40]
    print(f"\nSum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print(f"\nFib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    dispatch = spell_dispatcher()
    print(f"\n{dispatch(50)}")
    print(dispatch("Fireball"))
    print(dispatch([1, 2, 3]))

if __name__ == "__main__":
    main()