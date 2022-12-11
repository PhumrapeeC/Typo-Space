from games.rpg.components.status import DamageReduction, Enhanced, Vulnerability, Shattered, Regeneration, Exhaust, Poison
from typing import List
import random
from games.rpg.components.unit import Unit
from games.rpg.components.enemy import Enemy
import time


def damage_calculation(value):
    return 0 if value < 0 else value

class Warrior(Unit):
    def __init__(self, hp:float, attack:float, defense:float) -> None:
        super().__init__(hp,attack,defense)

    def beam_slash(self,enemy:Enemy):
        damage = self.total_attack() - enemy.total_defense()
        enemy.hp -= damage_calculation(damage)
        print(f"Warrior use: Beam Slash deal {damage_calculation(damage)}")

    def energy_shield(self):
        self.add_buff(DamageReduction(1,2))
        print(f"Warrior use: Energy Sheild, Damage Reduction 1 stack for 2 turns")
    
    def brave_rush(self, enemy:Enemy):
        # might change 20 to variable
        damage = 50 - enemy.total_defense()
        enemy.hp -= damage_calculation(damage)
        self.add_buff(Enhanced(1,3))
        print(f"Warrior use: Brave Rush deal {damage_calculation(damage)} and Enhanced 1 stack for 3 turns")

    def armor_break(self,enemy:Enemy):
        damage = 100 - enemy.total_defense()
        enemy.hp -= damage_calculation(damage)
        enemy.add_debuff(Vulnerability(1,3))
        print(f"Warrior use: Armor Break deal {damage_calculation(damage)} give enemy Vulnerability 1 stack for 3 turns")

    def get_move(self,move,enemies=None):
        if move == 1:
            self.beam_slash(enemies)
        elif move == 2:
            self.energy_shield()
        elif move == 3:
            self.brave_rush(enemies)
        elif move == 4:
            self.armor_break(enemies)

    def select_move(self,move):
        if move == 1:
            return {"move": "single target"}
        elif move == 2:
            return {"move": "none target"}
        elif move == 3:
            return {"move": "single target"}
        elif move == 4:
            return {"move": "single target"}

    def show_move(self):
        print("""
        [1] Beam Slash
        [2] Energy Sheild
        [3] Brave Rush 
        [4] Armor Break
        """)

    def __str__(self) -> str:
        return f"Warrior: hp: {self.hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"
            
class Trooper(Unit):
    def __init__(self, hp: float, attack: float, defense: float) -> None:
        super().__init__(hp, attack, defense)

    def beam_rifile(self, enemy:Enemy):
        print("Trooper use: Beam Rifle deal damage to enemy 3 times")
        for i in range(3):
            time.sleep(1.5)
            random_bullet = random.randint(20, 100)
            damage = random_bullet - enemy.total_defense()
            enemy.hp -= damage_calculation(damage)
            print(f"Beam rifle {i+1}: deal {damage_calculation(damage)}")

    def beam_overchage(self, enemy: Enemy):
        damage = 50
        enemy.hp -= damage
        print("Trooper use: Beam Overcharge deal 50 damage without calculate defense")

    def reload(self):
        self.add_buff(Enhanced(1,3))
        print("Trooper use: Reload, Enhanced 1 stack for 3 turns")
    
    def emergency_protocol(self):
        self.hp += 0.2 * self.based_hp
        print("Trooper use: Emergency Protocol, heal 20 percents of full health")

    def get_move(self,move,enemies=None):
        if move == 1:
            self.beam_rifile(enemies)
        elif move == 2:
            self.beam_overchage(enemies)
        elif move == 3:
            self.reload()
        elif move == 4:
            self.emergency_protocol()

    def select_move(self,move):
        if move == 1:
            return {"move": "single target"}
        elif move == 2:
            return {"move": "single target"}
        elif move == 3:
            return {"move": "none target"}
        elif move == 4:
            return {"move": "none target"}

    def show_move(self):
        print("""
        [1] Beam Rifle
        [2] Beam Overcharge
        [3] Reload
        [4] Emergency Protocol
        """)


    def __str__(self) -> str:
        return f"Trooper: hp: {self.hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"

class LifeForm(Unit):
    def __init__(self, hp: float, attack: float, defense: float) -> None:
        super().__init__(hp, attack, defense)

    def gloo_punch(self, enemy: Enemy):
        damage = 50 - enemy.total_defense()
        enemy.hp -= damage_calculation(damage)
        print(f"LifeForm use: Gloo Punch deal {damage_calculation(damage)}")

    def harden(self):
        self.add_buff(DamageReduction(2,2))
        self.add_debuff(Exhaust(2,2))
        print("LifeForm use: Harden, Damage Reduction 2 stacks for 2 turns but Exhaust 2 stacks for 2 turns")

    def acid_split(self, enemies:List[Enemy]):
        for enemy in enemies:
            enemy.add_debuff(Poison(1,2))
        print("LifeForm use: Acid Split, enemies receive Poison 1 stack 1 turn")

    def mysterious_chemical(self):
        self.add_buff(Enhanced(2,2))
        self.hp += 0.05 * self.based_hp
        print("LifeForm use: Mysterious Chemical, Enhanced 2 stacks for 2 turns and heal 5 percents from full health")

    def get_move(self,move,enemies=None):
        if move == 1:
            self.gloo_punch(enemies)
        elif move == 2:
            self.harden()
        elif move == 3:
            self.acid_split(enemies)
        elif move == 4:
            self.mysterious_chemical()


    def select_move(self,move):
        if move == 1:
            return {"move": "single target"}
        elif move == 2:
            return {"move": "none target"}
        elif move == 3:
            return {"move": "multi target"}
        elif move == 4:
            return {"move": "none target"}

    def show_move(self):
        print("""
        [1] Gloo Punch
        [2] Harden
        [3] Acid Split 
        [4] Mysterious Chemical
        """)

    def __str__(self) -> str:
        return f"LifeForm: hp: {self.hp}, attack: {self.total_attack()}, defense: {self.total_defense()}"


        


        

        
        

        



        
        

        
    
            


    
        