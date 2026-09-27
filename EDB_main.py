import math
import random

from psutil import process_iter


#CLASSES
class Player:
    def __init__(self, hp: float, atk: float):
        self.hp = hp
        # self.shield = shield (adding later..)
        self.atk = atk

        self.equipment: dict = {"sword": None, "shield_item": None, "armor": None}
        self.lvl: int = 1
        self.xp: int = 0

class Enemy:
    def __init__(self, hp: float, atk: float):
        self.hp = hp
        self.atk = atk

class Item:
    def __init__(self, name: str, item_type: str, stat_boost: float, rarity: str):
        self.name = name
        self.item_type = item_type
        self.stat_boost = stat_boost
        self.rarity = rarity

        if rarity not in rarities:
            raise ValueError(f"{rarity} is invalid item rarity")

        match item_type:
            case "Weapon":
                pass
            case "Armor":
                pass
            case _:
                raise ValueError(f"{item_type} is invalid item type")
    def __str__(self):
        return f"{self.name} ({self.rarity} {self.item_type}, +{self.stat_boost})"
    def __repr__(self):
        return self.__str__()

class Room:
    def __init__(self, room_type: str, doors: dict):
        self.type = room_type
        self.doors = doors
        if (self.type == "boss" or self.type == "miniboss") and len(doors) != 1:
            raise ValueError("Door amount not valid, (mini)boss should only have 1 door")

class RoomGenerator:
    def __init__(self, total_rooms):
        self.total_rooms: int = total_rooms
        self.boss_room: int = self.total_rooms
        self.miniboss_room: int = math.ceil(self.boss_room/2)
        self.rooms = []
        for room in range(1, self.total_rooms + 1):
            if room == self.boss_room:
                self.rooms.append(Room("boss", {1: None}))
            elif room == self.miniboss_room:
                self.rooms.append(Room("miniboss", {1: None}))
            else:
                random_room_type = random.choice(["Enemy", "Item", "Trap", "Empty"])
                self.rooms.append(Room(random_room_type, {1: None, 2: None}))

#FUNCTIONS
def battle(player, enemy):
    while True:
        choice = input("Attack or Flee(A/F): ").strip().upper()
        match choice:
            case "A":
                enemy.hp -= player.atk #Player attacks
                print(f"You hit enemy for -{player.atk}HP. Enemy HP: {enemy.hp}")

                if alive_checker(player.hp, enemy.hp) == "dead enemy":
                    break

                player.hp -= enemy.atk  #Enemy attacks
                print(f"You got hit by enemy for -{enemy.atk}HP. Your HP: {player.hp}")

                if alive_checker(player.hp, enemy.hp) == "dead player":
                    break
            case "F":
                player.hp -= enemy.atk
                print(f"While trying to flee, you got hit by enemy for -{enemy.atk}HP. Your HP: {player.hp}")
                break
            case _:
                print(f"{choice} not valid dummy, try again.")
    result = alive_checker(player.hp, enemy.hp)
    match result:
        case "dead enemy": #Defeated enemy
            enemy.hp = 0
            return "You win"
        case "dead player":
            player.hp = 0
            return "You died"
        case "All alive": #Survived while fleeing
            return "You survived"
        case _:
            raise RuntimeError(f"This result: {result} should not be possible")


def alive_checker(player_hp, enemy_hp):
    if player_hp <= 0 and enemy_hp <= 0:
        raise RuntimeError("Player and enemy should not be dead at same time.")
    elif player_hp <= 0:
        return "dead player"
    elif enemy_hp <= 0:
        return "dead enemy"
    else:
        return "All alive"

def item_roller(rarity: str, amount: int):
    if amount < 1:
        raise ValueError("Amount should be 1 at least")

    matching_items = [item for item in item_list if item.rarity == rarity]
    roll_items = []
    for item in range(amount):
        index = random.randint(0, len(matching_items) - 1)
        roll_items.append(matching_items[index])
        #temp
    return roll_items, matching_items




#DATA
rarities = ["Trash", "Poor", "Standard", "Good", "Great", "Super", "Perfect"]

weapons = [ #temp stat_boost value, adjust later
    Item("Wooden Shard", "Weapon", 1, "Trash"),
    Item("Chipped Stone", "Weapon", 2, "Trash"),
    Item("Scrap Knife", "Weapon", 3, "Trash"),
    Item("Bent Pipe", "Weapon", 4, "Trash"),
    Item("Dull Cleaver", "Weapon", 8, "Poor"),
    Item("Old Hunting Knife", "Weapon", 10, "Poor"),
    Item("Bronze Dagger", "Weapon", 12, "Poor"),
    Item("Rusted Iron Blade", "Weapon", 14, "Poor")
]
armor = [   #temp stat_boost value, adjust later
    Item("Cardboard Vest", "Armor", 1, "Trash"),
    Item("Thick Canvas Wrap", "Armor", 2, "Trash"),
    Item("Plastic Trash Lid", "Armor", 3, "Trash"),
    Item("Ripped Leather Jacket", "Armor", 4, "Trash"),
    Item("Burlap & Chain Mail", "Armor", 8, "Poor"),
    Item("Padded Work Vest", "Armor", 10, "Poor"),
    Item("Boiled Leather Scraps", "Armor", 12, "Poor"),
    Item("Rusted Scrap Breastplate", "Armor", 14, "Poor")
]

item_list = weapons + armor



#TESTING

print(item_roller("Trash", 3))

Player1 = Player(100,25)
Zombie = Enemy(67, 40)
battle_result = battle(Player1, Zombie)
print(battle_result)
print(f"Player hp: {Player1.hp}, Enemy.hp: {Zombie.hp}")


