from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def incrementer() -> int:
        nonlocal count
        count += 1
        return count

    return incrementer


def spell_accumulator(initial_power: int) -> Callable:
    if not isinstance(initial_power, int):
        def handle_error() -> str:
            return "Power must be an integer"
        return handle_error

    current_power = initial_power

    def accumulate_power(power: int) -> int | str:
        try:
            nonlocal current_power
            current_power += power
            return current_power
        except (TypeError, ValueError):
            return "Power must be an integer"

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def create_enchanted_description(item: str) -> str:
        try:
            enchantment_description = f"{enchantment_type} {item}"
            return enchantment_description
        except Exception:
            return "Enchantment failed"

    return create_enchanted_description


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        try:
            vault[key] = value
        except Exception:
            print("Cannot store in dictionnary")

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:

    print("Testing mage counter...")

    counter = mage_counter()

    for i in range(1, 4):
        print(f"call {i} {counter()}")

    print("\nTesting spell accumulator...")

    start_power = 0
    accumulator = spell_accumulator(start_power)
    print(f"At the beginning, total power = {start_power}")
    initial_powers = [79, 66, 78]
    for p in initial_powers:
        print(f"add {p} : total power = {accumulator(p)}")

    print("\nTesting enchantment factory...")

    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    result_fire = fire_factory("Sword")
    result_ice = ice_factory("Shield")
    print(f"{result_fire}")
    print(f"{result_ice}")

    print("\nTesting memory vault...")

    vault = memory_vault()
    vault['store']("my secret artifact", "my secret spell")
    print(f"Recall secret: {vault['recall']('my secret artifact')}")
    print(f"Recall unknown: {vault['recall']('my secret password')}")


if __name__ == "__main__":
    main()
