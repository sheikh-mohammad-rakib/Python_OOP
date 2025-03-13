class Person:
    def __init__(self, name, age):
        self.name = name      # Public attribute
        self._age = age       # Protected attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive!")

# Creating an object
person = Person("Alice", 30)

# Accessing public attribute
print(person.name)  # Output: Alice

# Accessing protected attribute (not recommended)
print(person._age)  # Output: 30

# Using getter and setter methods
print(person.get_age())  # Output: 30
person.set_age(35)
print(person.get_age())  # Output: 35
person.set_age(-5)       # Output: Age must be positive!