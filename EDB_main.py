import math
import random


class Player:
    def __init__(self, hp: float, shield:float, attack: float):
        self.hp = hp
        self.shield = shield
        self.attack = attack

        self.equipment: dict = {"sword": None, "shield_item": None, "armor": None}
        self.lvl: int = 1
        self.xp: int = 0

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
Lvl1_dungeon = RoomGenerator(10)
for room in Lvl1_dungeon.rooms:
    print(room.type, room.doors)



