class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Sparrow(Bird):
    def fly(self):
        return f"{self.name} flies short distances."

class Eagle(Bird):
    def fly(self):
        return f"{self.name} flies high and far."

# Polymorphism in action
birds = [Sparrow("Jack"), Eagle("Baldie")]

for bird in birds:
    print(bird.fly())
    # Output:
    # Jack flies short distances.
    # Baldie flies high and far.