class Car:
    # Class attribute
    wheels = 4

    # Initializer / Instance attributes
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Instance method
    def description(self):
        return f"{self.make} {self.model} has {Car.wheels} wheels."

# Creating objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# Accessing instance attributes
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Accord

# Accessing class attributes
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Calling instance methods
print(car1.description())  # Output: Toyota Camry has 4 wheels.
print(car2.description())  # Output: Honda Accord has 4 wheels.