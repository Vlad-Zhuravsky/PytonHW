from time import sleep

class TrafficLight:
    __color = "Черный"

    def run(self):
        while True:
            print("Зеленый")
            sleep(10)
            print("Желтый")
            sleep(2)
            print("Красный")
            sleep(10)

traficlight = TrafficLight()
traficlight.run()