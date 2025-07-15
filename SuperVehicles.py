# Base class for all vehicles
class Vehicle:
    def __init__(self, name, mpg):
    # Set the name and mpg (miles per gallon) for the vehicle 
        self.name = name
        self.mpg = mpg  # miles per gallon

    def fuel_needed(self, distance):
         # Calculates how much fuel is needed for a given distance
        result =  distance / self.mpg
        return result

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."


class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 30)


class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)


class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 