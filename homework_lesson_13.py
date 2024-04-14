# task 1

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection(metaclass=Singleton):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


db_connection1 = DBConnection("user1", "password1")
db_connection2 = DBConnection("user2", "password2")

print(db_connection1 is db_connection2)
