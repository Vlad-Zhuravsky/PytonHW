class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"доход": salary, "премия": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{self.income.values()}"

manager = Position("Влад", "Миронов", "Дизайнер", "650000", "15000")
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())