# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/12 16:33:38 by steph           #+#    #+#               #
#  Updated: 2026/03/13 08:46:36 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
        )
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(
        filter(lambda mage: mage["power"] >= min_power, mages)
        )
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda x: f"*{x}*", spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
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
