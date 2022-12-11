from games.rpg.components.unit import Unit
from games.rpg.components.status import Enhanced, Exhaust, DamageReduction
from typing import List

def damage_calculation(value):
    return 0 if value < 0 else value

class Enemy(Unit):
    def __init__(self, hp: float, attack: float, defense: float) -> None:
        super().__init__(hp, attack, defense)
        self.move_set = []

class Crook(Enemy):
    def __init__(self, hp: float, attack: float, defense: float, move_set: List ) -> None:
        super().__init__(hp, attack, defense)
        self.name = "Crook"
        self.move_set = move_set

    def pistol(self, player:Unit):
        damage = 50 - player.total_defense()
        player.__hp -= damage_calculation(damage)
        print(f"Crook use: Pistol deal {damage_calculation(damage)}")

    def warcry(self):
        self.add_buff(Enhanced(1,2))
        print("Crook use: Warcry, Enhance 1 stack for 2 turns")

    def select_move(self, enemies):
        move = self.move_set[0]
        self.move_set.pop(0)
        self.move_set.append(move)
        if move == 1:
            self.pistol(enemies)

        elif move == 2:
            self.warcry()

    def __str__(self) -> str:
        return f"Crook: hp: {self.__hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"

class StrayDog(Enemy):
    def __init__(self, hp: float, attack: float, defense: float, move_set: List) -> None:
        super().__init__(hp, attack, defense)
        self.name = "Stray Dog"
        self.move_set = move_set

    def bite(self, player):
        damage = 50 - player.total_defense()
        player.hp -= damage_calculation(damage)
        print(f"Stray Dog use: Bite deal {damage_calculation(damage)}")

    def howl(self, player: Unit):
        player.add_debuff(Exhaust(1,1))
        print(f"Stray Dog use: howl give player Exhuast 1 stack for 1 turn")

    def select_move(self, enemies):
        move = self.move_set[0]
        self.move_set.pop(0)
        self.move_set.append(move)
        if move == 1:
            self.bite(enemies)

        elif move == 2:
            self.howl(enemies)

    def __str__(self) -> str:
        return f"StaryDog: hp: {self.__hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"


class OutlawKing(Enemy):
    def __init__(self, hp: float, attack: float, defense: float, move_set: List) -> None:
        super().__init__(hp, attack, defense)
        self.name = "Outlaw King"
        self.move_set = move_set

    def double_shoot(self, player):
        damage = 100 - player.total_defense()
        player.hp -= damage_calculation(damage)
        print(f"Outlaw King use: Double Shoot deal {damage_calculation(damage)}")

    def junk_power(self):
        self.add_buff(Enhanced(2,2))
        self.add_buff(DamageReduction(2,2))
        print(f"Outlaw King use: Junk Power, Enhanced 2 stacks for 2 turns and Damage Reduction 2 stacks for 2 turns")

    def drill_charge(self, player):
        damage = 200 - player.total_defense()
        player.hp -= damage_calculation(damage)
        print(f"Outlaw King use: Drill Charge deal {damage_calculation(damage)}")

    def select_move(self, enemies):
        move = self.move_set[0]
        self.move_set.pop(0)
        self.move_set.append(move)
        if move == 1:
            self.double_shoot(enemies)

        elif move == 2:
            self.junk_power()

        elif move == 3:
            self.drill_charge(enemies)

    def __str__(self) -> str:
        return f"Outlaw King: hp: {self.__hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"

