string = input("Введите слова через пробелы: ").strip()
for i, word in enumerate(string, 1):
    print(f"{i}, {word[:10]}")