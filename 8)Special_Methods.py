class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Creating objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using special methods
print(p1)  # Output: Point(2, 3)
p3 = p1 + p2
print(p3)  # Output: Point(6, 8)
print(p1 == p2)  # Output: False