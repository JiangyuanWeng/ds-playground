import math

class DataPoint:
    def __init__(self, x :int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f'该点的坐标是({self.x}, {self.y})'

    def compare(self, other1, other2):
        distance1 = self.distance_to(other1)
        distance2 = self.distance_to(other2)
        if distance1 >= distance2:
            return f'远的点是{(other1.x, other1.y)}'
        else:
            return f'远的点是{(other2.x, other2.y)}'

#
# p1 = DataPoint(1, 1)
# p2 = DataPoint(3, 3)
#
# print(p1.distance_to(p2))

