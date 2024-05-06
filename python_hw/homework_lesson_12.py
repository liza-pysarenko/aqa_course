# task 1

from abc import ABC, abstractmethod


class AbstractDevice(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class ConcreteDevice(AbstractDevice):

    def turn_on(self):
        return "Turning on the device"

    def turn_off(self):
        return "Turning off the device"


concrete_device = ConcreteDevice()

print(concrete_device.turn_on())
print(concrete_device.turn_off())


# task 2

class TV:

    def turn_on(self):
        return "TV is turned on"

    def turn_off(self):
        return "TV is turned off"


class Lights:

    def turn_on(self):
        return "Lights are turned on"

    def turn_off(self):
        return "Lights are turned off"


class Heating:

    def turn_on(self):
        return "Heating is turned on"

    def turn_off(self):
        return "Heating is turned off"


class HomeFacade:

    def __init__(self):
        self.tv = TV()
        self.lights = Lights()
        self.heating = Heating()

    def come_home(self):
        return f"{self.tv.turn_on()}, {self.lights.turn_on()} and {self.heating.turn_on()} when coming home."

    def go_out(self):
        return f"{self.tv.turn_off()}, {self.lights.turn_off()} and {self.heating.turn_off()} when going out."


facade = HomeFacade()

print(facade.come_home())
print(facade.go_out())


# task 3

class MyContextManager:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        print(f"Opening resource: {self.resource}")
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing resource: {self.resource}")


with MyContextManager("database connection") as connection:
        print(f"Using resource: {connection}")
