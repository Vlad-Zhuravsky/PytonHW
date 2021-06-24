class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} * {self._width} * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000}"

road_1 = Road(1000,15)
print(road_1.get_full_profit())

