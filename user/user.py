class User:
    def __init__(self, username, password, name) -> None:
        self.username = username
        self.__password = password
        self.name = name

    def check_password(self, password):
        return password == self.__password

    def get_list_user(self):
        return [self.username, self.__password, self.name]

    def __str__(self):
        return f"{self.username},{self.__password},{self.name}"
