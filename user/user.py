class User:
    def __init__(self, username, password, name) -> None:
        self.__username = username
        self.__password = password
        self.name = name

    def check_password(self, password):
        return password == self.__password

    def get_list_user(self):
        return [self.__username, self.__password, self.name]

    def __str__(self):
        return f"{self.__username},{self.__password},{self.name}"
