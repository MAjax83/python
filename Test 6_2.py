class Road:
    _length = None
    _width = None
    _mass = 25
    _depth = 0.05

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self._mass * self._depth


road = Road(length=5000, width=20)
print(road.calculate())