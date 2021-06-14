def sum_num():
    s = 0
    while True:
        in_list = input("Введите число Q для выхода: ").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                s += int(num)
        print(f"Сумма чисел = {s}")