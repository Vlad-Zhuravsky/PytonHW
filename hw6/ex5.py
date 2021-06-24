class Stationary:

    def __init__(self, title="Что-то, что может рисовать"):
        self.title = title

    def draw(self):
        print(f"{self.title} начинает рисовать")

class Pen(Stationary):

    def draw(self):
        print(f"{self.title} рисует ручкой")

class Pencil(Stationary):

    def draw(self):
        print(f"{self.title} рисует карандашом")

class Handle(Stationary):

    def draw(self):
        print(f"{self.title} рисует маркером")

stat = Stationary()
stat.draw()

pen = Pen()
pen.draw()