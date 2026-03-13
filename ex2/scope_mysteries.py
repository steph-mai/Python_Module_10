from typing import Callable, Any

def mage_counter() -> Callable[[], int]:
    """
    Crée un compteur magique persistant sans variables globales
    """
    count = 0  
    
    def counter() -> int:
        nonlocal count  
        count += 1
        return count
    
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Crée un accumulateur de puissance magique.
    """
    total_power = initial_power  
    
    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power  
        return total_power
    
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Fabrique des fonctions d'enchantement spécifiques.
    """
    def enchant(item_name: str) -> str:
       
        return f"{enchantment_type} {item_name}"
    
    return enchant


def memory_vault() -> dict[str, Callable]:
    """
    Crée un système de gestion de mémoire privée via une closure.
    """
    vault = {} 
    
    def store(key: str, value: Any) -> None:
        """Enregistre une valeur dans la mémoire."""
        vault[key] = value
        
    def recall(key: str) -> Any:
        """Récupère une valeur ou indique si elle est absente."""
        return vault.get(key, "Memory not found")
    
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
   
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")  
    print(f"Call 2: {counter()}")  
    print(f"Call 3: {counter()}")  


    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Adding 50: {acc(50)}")   
    print(f"Adding 25: {acc(25)}")   

   
    print("\nTesting enchantment factory...")
    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    print(fire_factory("Sword"))  
    print(ice_factory("Shield"))  


    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("secret_spell", "Abra Kadabra")
    print(f"Recall secret: {vault['recall']('secret_spell')}")
    print(f"Recall unknown: {vault['recall']('lost_scroll')}")

if __name__ == "__main__":
    main()