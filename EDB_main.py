import math
import random

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


#TESTING

Player1 = Player(100,25)
Zombie = Enemy(67, 40)
battle_result = battle(Player1, Zombie)
print(battle_result)
print(f"Player hp: {Player1.hp}, Enemy.hp: {Zombie.hp}")


