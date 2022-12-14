from games.rpg.components.status import Status, Shattered
class Unit:
    def __init__(self, hp:float, attack:float, defense:float) -> None:
        self.based_hp = hp
        self.hp = hp
        self.attack = attack # current attack 
        self.defense = defense # current defense
        self.additional_attack = 0 #additional attack can be either positive or negative
        self.additional_defense = 0 # addtional defense can be either positive or negative
        self.buff = [] # list of buff
        self.debuff = [] # list of debuff
        self.is_attack = False #Check if attack or not
        self.can_attack = True #Check if can attack or not
        self.count_attacked = 0 #Count of damage receive

    def total_defense(self):
        return self.defense + self.additional_defense

    def total_attack(self):
        return self.attack + self.additional_attack

    def update_status(self):
        remove_buff = []
        remove_debuff = []
        for buff in self.buff:
            if buff.turn > 0:
                buff.activate(self)
                buff.decrease_turn()
            else:
                remove_buff.append(buff)

        for debuff in self.debuff:
            if debuff.turn > 0:
                debuff.activate(self)
            else:
                remove_debuff.append(debuff)
            if not type(debuff) == Shattered:
                debuff.decrease_turn()

        for b in remove_buff:
            self.buff.remove(b)

        for db in remove_debuff:
            self.debuff.remove(db)

        for i in self.buff:
            print(i)
        for j in self.debuff:
            print(j)

        

    def add_buff(self,receive_buff:Status):
        check = False
        for buff in self.buff:
            if type(receive_buff) == type(buff):
                buff.stack_up(receive_buff.stack)
                buff.increase_turn(receive_buff.turn)
                check = True
        if not check:
            self.buff.append(receive_buff)

    def add_debuff(self, receive_debuff:Status):
        check = False
        for debuff in self.debuff:
            if type(receive_debuff) == type(debuff):
                debuff.stack_up(receive_debuff.stack)
                debuff.increase_turn(receive_debuff.turn)
                check = True
        if not check:
            self.debuff.append(receive_debuff)

    def is_defeat(self):
        return self.hp <= 0