from user.db import DB
from games.rpg.turn_base_rpg import play_rpg

database = DB("data/user.csv")
user_session = {"user": "", "login": False}
print("_̲_̲_̲_̲_̲ _̲_̲_̲_̲_̲ _̲_̲_̲_̲_̲_̲_̲_̲_̲ _̲_̲_̲_̲_̲_̲   WELCOME TO  _̲_̲_̲_̲_̲ _̲_̲_̲_̲_̲_̲_̲_̲_̲_̲__̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲_̲ ")
print(""" 
████████╗██╗░░░██╗██████╗░░█████╗░  ░██████╗██████╗░░█████╗░░█████╗░███████╗
╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
░░░██║░░░░╚████╔╝░██████╔╝██║░░██║  ╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░
░░░██║░░░░░╚██╔╝░░██╔═══╝░██║░░██║  ░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░
░░░██║░░░░░░██║░░░██║░░░░░╚█████╔╝  ██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░╚════╝░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝
""")
print("_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷_̷")
print()
while True:
    if user_session["user"] == "" and user_session["login"] == False:
        while True:
            try:
                authen = int(input("[1] Login or [2] Signup or [3] Quit: "))
                if authen < 1 or authen > 3:
                    print("Choose only the choices that are given!!")
                else:
                    break
            except ValueError:
                print("Only numbers are allowed")

        if authen == 1:
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print(f'|{"Please login here.": ^25}|')
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if database.login(username, password):
                    print("Successful Login")
                    user_session["user"] = username
                    user_session["login"] = True
                    break
                else:
                    print("Wrong username or password")
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")

        elif authen == 2:
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            print(f'|{"Please signup here.": ^25}|')
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
            while True:
                username = input("Username: ")
                password = input("Password: ")
                name = input("name: ")
                if database.register(username, password, name):
                    print(f"User created success: {username}")
                    user_session["user"] = username
                    user_session["login"] = True
                    break
                else:
                    print("Already has this username in system!!")
            print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")

        elif authen == 3:
            print("""
                ░██████╗░░█████╗░░█████╗░██████╗░  ██████╗░██╗░░░██╗███████╗
                ██╔════╝░██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗╚██╗░██╔╝██╔════╝
                ██║░░██╗░██║░░██║██║░░██║██║░░██║  ██████╦╝░╚████╔╝░█████╗░░
                ██║░░╚██╗██║░░██║██║░░██║██║░░██║  ██╔══██╗░░╚██╔╝░░██╔══╝░░
                ╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝  ██████╦╝░░░██║░░░███████╗
                ░╚═════╝░░╚════╝░░╚════╝░╚═════╝░  ╚═════╝░░░░╚═╝░░░╚══════╝
            """)
            break

    else:
        welcome = f"Welcome {user_session['user']}"
        print(f"{welcome: ^25}")
        print("₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋")
        while True:
            try:
                choice = int(input("[1] play game or [2] logout: "))
                if choice < 1 or choice >= 3:
                    print("Choose only the choices that are given!!")
                else:
                    break
            except ValueError:
                print("Only numbers are allowed")
        if choice == 1:
            play_rpg()
        elif choice == 2:
            user_session["user"] = ""
            user_session["login"] = False
            database.update_db()
