class Car:

    def __init__(self, name, color, speed, is_police = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: машина поехала")

    def stop(self):
        print(f"{self.name}: машина остановилась")

    def turn(self):
        print(f"{self.name}: машина повернула")

    def show_speed(self):
        print(f"{self.name}: скорость {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name} скорость {self.speed} - Превышение Скорости" \
        if self.speed > 40 else f"{self.name} скорость {self.speed}"
class SportCar(Car):

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)