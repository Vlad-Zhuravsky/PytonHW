from sys import argv

def salary():
    time, rate, bonus = map(float, argv[1:])
    print(f"Зарплата: {time * rate + bonus}")

salary()