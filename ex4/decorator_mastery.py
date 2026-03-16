# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 13:18:10 by stmaire         #+#    #+#               #
#  Updated: 2026/03/16 16:00:50 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import functools
import time
from typing import Callable, Any


def spell_timer(function: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {function.__name__}...")
        start_time = time.time()
        result = function(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any]
]:
    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power", args[-1] if args else None)
            if power is None or not isinstance(power, int):
                return "Power mus be a positive integer"
            elif power < min_power:
                return "Insufficient power for this spell"
            return function(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any]
]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (
            len(name) >= 3
            and all(
                char.isspace()
                or char.isalpha()
                for char in name)
        ):
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:

    print("\nTesting spell timer...")

    @spell_timer
    def cast_fireball() -> str:
        return "Casting fireball"
    print(cast_fireball())
    print("Result: Fireball cast!")

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=3)
    def failing_spell():
        raise Exception("Fail")

    print(failing_spell())

    print("\nTesting MageGuild...")

    guild = MageGuild()
    print(MageGuild.validate_mage_name("Lorely"))
    print(MageGuild.validate_mage_name("Ix"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice", 5))


if __name__ == "__main__":
    main()
