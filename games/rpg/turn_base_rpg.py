from games.rpg.components.clan import Warrior, Trooper, LifeForm
from games.rpg.components.enemy import Crook, StrayDog, OutlawKing
from games.type.typing_game import play
import json
import time

clan_file = open("data/clan.json")
data_clan = json.load(clan_file)

enemy_file = open("data/enemy.json")
data_enemy = json.load(enemy_file)

level_file = open("data/level.json")
data_level = json.load(level_file)

def init_enemy(name):
    if name == "Crook":
        crook = data_enemy["Crook"]
        return Crook(crook["hp"], crook["attack"], crook["defense"], crook["move_set"])

    elif name == "StrayDog":
        stray_dog = data_enemy["StrayDog"]
        return StrayDog(stray_dog["hp"], stray_dog["attack"], stray_dog["defense"], stray_dog["move_set"])
    
    elif name == "Outlaw King":
        outlaw_king = data_enemy["Outlaw King"]
        return OutlawKing(outlaw_king["hp"], outlaw_king["attack"], outlaw_king["defense"], outlaw_king["move_set"])

def init_level(num):
    enemies = []
    level = ""
    if num == 1:
        level = "Easy"
    elif num == 2:
        level = "Normal"
    elif num == 3:
        level = "Hard"

    for i in data_level[level]:
        temp = init_enemy(i)
        enemies.append(temp)

    return enemies

def init_character(num):
    if num ==  1:
        data_warrior = data_clan["Warrior"]
        return Warrior(data_warrior["hp"], data_warrior["attack"], data_warrior["defense"])

    elif num == 2:
        data_trooper = data_clan["Trooper"]
        return Trooper(data_trooper["hp"], data_trooper["attack"], data_trooper["defense"])

    elif num == 3:
        data_lifeform = data_clan["LifeForm"]
        return LifeForm(data_lifeform["hp"], data_lifeform["attack"], data_lifeform["defense"])

def play_rpg():
    while True:
        choice = input("[P]lay or [Q]uit?: ")
        if choice.lower() == "q":
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            break
        elif choice.lower() == "p":
            turn = 1
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print(f'|{"Choose your charater.": ^25}|')
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print("[1] Warrior")
            print("[2] Trooper")
            print("[3] LifeForm")
            while True:
                try:
                    print("_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲")
                    num = int(input("Character selected: "))
                    if num < 1 or num > 3:
                        print("Choose only the choices that are given!!")
                    else:
                        break
                except ValueError:
                    print("Only numbers are allowed")
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n")
            character = init_character(num)
            
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print(f'|{"Choose Level.": ^25}|')
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print("[1] Easy")
            print("[2] Normal")
            print("[3] Hard")
            while True:
                try:
                    print("_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲")
                    level = int(input("level selected: "))
                    if level < 1 or level > 3:
                        print("Choose only the choices that are given!!")
                    else:
                        break
                except ValueError:
                    print("Only numbers are allowed")
            enemies = init_level(level)
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n")

            while True:
                defeat_enemies = []
                for e in enemies:
                    if e.is_defeat():
                        defeat_enemies.append(e)
                for de in defeat_enemies:
                    enemies.remove(de)
                    print(f"{de.name} has been defeated")
                print(f"Turn: {turn}")
                print(f"Enemy lefts: {len(enemies)}")
                if turn % 2 != 0:
                    print(character)
                    while True:
                        try:
                            character.show_move()
                            move = int(input("Select move: "))
                            if move < 1 or move > 4:
                                print("Choose only the choices that are given!!")
                            else:
                                break
                        except ValueError:
                            print("Only numbers are allowed")
                    character_move = character.select_move(move)
                    wpm = play()
                    if wpm > 20:
                        time.sleep(1.5)
                        if character_move["move"] == "single target":
                            print("Choose Enemy")
                            for i in range(len(enemies)):
                                print(f"[{i+1}] {enemies[i]}")
                            while True:
                                try:
                                    print("_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲")
                                    num_enemy = int(input("Selected enemy: "))
                                    if num_enemy > len(enemies):
                                        print("Choose only the choices that are given!!")
                                    else:
                                        break
                                except ValueError:
                                    print("Only numbers are allowed")
                            enemy = enemies[num_enemy - 1]
                            character.get_move(move, enemy)
                        elif character_move["move"] == "multi target":
                            character.get_move(move, enemies)

                        elif character_move["move"] == "none target":
                            character.get_move(move)
                        time.sleep(1.5)
                    else:
                        print("----Activate move failed----")
                    character.update_status()
                    time.sleep(1.5)

                elif turn % 2 == 0:
                    for enemy in enemies:
                        print(enemy)
                        time.sleep(1.5)
                        enemy.select_move(character)
                        enemy.update_status()
                    print()
                    
                if character.is_defeat():
                    print("Game Over")
                    print("You have been defeated")
                    break
                
                elif len(enemies) == 0:
                    print("You Win")
                    break

                turn += 1
                