# task 1

class Ship:

    def __init__(self, name: str, capacity: int):
        self._name = name
        self._capacity = capacity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    def move(self):
        return f"{self.name} is moving."


ship = Ship("Black Pearl", 25)
print(ship.move())


# task 2

class Liner(Ship):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    def entertainment(self):
        return "Watching the \"Pirates of the Caribbean\" movie."


liner = Liner("Allure of the Seas", 6296)
print(liner.move())
print(liner.entertainment())
