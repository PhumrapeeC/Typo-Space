class Status:
    def __init__(self, stack:int, turn:int):
        self.stack = stack
        self.turn = turn

    def stack_up(self, stack = 1):
        self.stack += stack

    def increase_turn(self, turn =1):
        self.turn += turn

    def decrease_turn(self):
        self.turn -= 1

    def activate(self, unit):
        pass

    def stack_down(self):
        self.stack -= 1


class DamageReduction(Status):
    def __init__(self, stack:int, turn:int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.additional_defense += 0.2 * self.stack

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Damage Reduction | stack: {self.stack} for {self.turn} {turn}"

class Enhanced(Status):
    def __init__(self, stack:int, turn:int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.additional_attack += 0.2 * self.stack

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Enhanced | stack: {self.stack} for {self.turn} {turn}"       

class Vulnerability(Status):
    def __init__(self, stack: int, turn: int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.additional_defense -= 0.2 * self.stack

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Vulnerability | stack: {self.stack} for {self.turn} {turn}" 

class Shattered(Status):
    def __init__(self, stack: int, turn: int):
        super().__init__(stack, turn)

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Shattered | stack: {self.stack} for {self.turn} {turn}" 

class Regeneration(Status):
    def __init__(self, stack: int, turn: int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.hp += 0.05 * self.based_hp * self.stack

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Regeneration | stack: {self.stack} for {self.turn} {turn}" 

class Exhaust(Status):
    def __init__(self, stack: int, turn: int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.additional_attack -= 0.2 * self.stack

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Exhaust | stack: {self.stack} for {self.turn} {turn}" 

class Poison(Status):
    def __init__(self, stack: int, turn: int):
        super().__init__(stack, turn)

    def activate(self, unit):
        unit.hp -= 0.03 * unit.based_hp

    def __str__(self) -> str:
        turn = "turns" if self.turn > 1 else "turn"
        return f"Poison | stack: {self.stack} for {self.turn} {turn}" 
    