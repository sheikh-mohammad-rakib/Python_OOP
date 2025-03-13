class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
my_dog = Dog("Rex", 3)
your_dog = Dog("Bo", 5)

print(my_dog.species)
print(your_dog.species)

print(my_dog.description())
print(my_dog.speak("Woof Woof"))

print(my_dog.speak("Bow Wow"))
print(your_dog.description())