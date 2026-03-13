import functools
import time
from typing import Callable, Any

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # On vérifie le premier argument positionnel (power)
            if args and args[0] >= min_power:
                return func(*args, **kwargs)
            # Cas spécifique pour les méthodes d'instance (self est en args[0])
            if len(args) > 1 and isinstance(args[1], (int, float)) and args[1] >= min_power:
                 return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"

def main() -> None:
    @spell_timer
    def slow_fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("\nTesting spell timer...")
    print(f"Result: {slow_fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Al"))
    print(MageGuild.validate_mage_name("Gandalf"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    @retry_spell(3)
    def unstable_spell():
        raise Exception("Mana leak")

    print("\nTesting retry spell...")
    print(unstable_spell())

if __name__ == "__main__":
    main()