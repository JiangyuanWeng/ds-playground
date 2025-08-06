import math

class DataPoint:
    def __init__(self, x :int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = DataPoint(1, 1)
p2 = DataPoint(3, 3)

print(p1.distance_to(p2))

