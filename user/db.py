import hashlib
from user.user import User
import csv

class DB:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.table = self.load_files()

    def load_files(self):
        db = {}
        with open(self.filename, "r") as files:
            skip = True
            lines = csv.reader(files)
            for i in lines:
                if skip or len(i) == 0:
                    skip = False
                    continue
                db[i[0]] = User(i[0],i[1],i[2])
            return db

    def register(self, username: str, password: str, name: str):
        if username not in self.table:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.table[username] = User(username, hashed_password, name)
            return True
        else:
            return False

    def login(self, username:str , password: str): # admin account -> username: admin, password: admin1234
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        try:
            return self.table[username].check_password(hashed_password)
        except KeyError:
            return False

    def update_db(self):
        header = ["username", "password", "name"]
        result = []
        for i in self.table:
            result.append(self.table[i].get_list_user())
        with open(self.filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(result)

    def get_table(self):
        return self.table

    def get_user(self, username: str):
        return self.table[username]

    def update_user(self, user: User):
        self.table[user.username] = user

    def __str__(self): # --> dashboard
        return ""