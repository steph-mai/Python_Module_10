# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/12 16:33:38 by steph           #+#    #+#               #
#  Updated: 2026/03/16 18:04:57 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact["power"],
            reverse=True
        )
    except (KeyError, TypeError) as e:
        print(f"Sorting failed: Missing or invalid 'power' key. Error: {e}")
        return []


def power_filter(
        mages: list[dict[str, Any]],
        min_power: int
        ) -> list[dict[str, Any]]:
    try:
        return list(
            filter(lambda m: int(m.get("power", 0)) >= min_power, mages)
        )
    except (TypeError, ValueError) as e:
        print(f"Invalid data: {e}.")
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda x: f"*{str(x)}*", spells))
    except Exception as e:
        print(f"Transformation failed: {e}")
        return []


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    nb_mages = len(mages)
    if nb_mages == 0:
        return {'max_power': 0, 'least_power': 0, 'avg_power': 0.00}

    max_power_mage = max(mages, key=lambda mage: mage.get("power", 0))
    least_power_mage = min(mages, key=lambda mage: mage.get("power", 0))

    total_power = sum(map(lambda mage: mage.get("power", 0), mages))

    average_power = round(total_power / nb_mages, 2)

    return {
        'max_power': max_power_mage.get("power", 0),
        'least_power': least_power_mage.get("power", 0),
        'avg_power': average_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Earth Shield', 'power': 72, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 61, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 111, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'accessory'}
        ]

    mages = [
        {'name': 'Luna', 'power': 91, 'element': 'lightning'},
        {'name': 'Oscar', 'power': 98, 'element': 'fire'},
        {'name': 'Zara', 'power': 101, 'element': 'shadow'},
        {'name': 'Jordan', 'power': 85, 'element': 'ice'},
        {'name': 'John', 'power': 98, 'element': 'lightning'}]

    spells = ['meteor', 'heal', 'darkness', 'freeze']

    print("\nTesting artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts)

    if len(sorted_artifacts) >= 2:
        first_artifact = sorted_artifacts[0]
        second_artifact = sorted_artifacts[1]
        print(f"{first_artifact['name']} ({first_artifact['power']} power) "
              f"comes before {second_artifact['name']} "
              f"({second_artifact['power']} power)")
    elif len(sorted_artifacts) == 1:
        print(f"Only one artifact found: {sorted_artifacts[0]['name']}")

    print("\nTesting mages filter...")

    filtered_mages = power_filter(mages, 97)
    mages_names = list(mage["name"] for mage in filtered_mages)
    clean_names = ", ".join(mages_names)
    print(f"{clean_names}")

    print("\nTesting spell transformer...")

    trans_spells = spell_transformer(spells)
    clean_spells = " ".join(trans_spells)
    print(f"{clean_spells}")

    print("\nTesting mages stats...")

    print(mage_stats(mages))


if __name__ == "__main__":
    main()
