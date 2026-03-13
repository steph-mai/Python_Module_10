# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/12 13:20:54 by stmaire         #+#    #+#               #
#  Updated: 2026/03/12 15:13:01 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key= lambda artifact: artifact["power"], reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filtered_mages

def spell_transformer(spells: list[str]) -> list[str]:


# def mage_stats(mages: list[dict]) -> dict:


def main() -> None:
    artifacts = [{'name': 'Storm Crown', 'power': 112, 'type': 'focus'}, {'name': 'Earth Shield', 'power': 91, 'type': 'weapon'}, {'name': 'Earth Shield', 'power': 60, 'type': 'weapon'}, {'name': 'Light Prism', 'power': 116, 'type': 'focus'}]
    mages = [{'name': 'Morgan', 'power': 92, 'element': 'light'}, {'name': 'Storm', 'power': 53, 'element': 'lightning'}, {'name': 'Kai', 'power': 56, 'element': 'fire'}, {'name': 'Ember', 'power': 79, 'element': 'wind'}, {'name': 'Luna', 'power': 98, 'element': 'water'}]
    # spells = ['tornado', 'tsunami', 'shield', 'flash']

    print(artifact_sorter(artifacts))
    print(power_filter(mages, 80))


if __name__ == "__main__":
    main()

