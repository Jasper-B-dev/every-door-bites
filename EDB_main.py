class Player:
    def __init__(self, hp: int, shield:int, attack: int):
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

room1 = Room("boss", {})



