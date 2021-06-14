def function(num_1, num_2):
    num_1, num_2 = int(num_1), int(num_2)
    result = num_1 / num_2
    return result

print(function(input("Введите первое число:"), input("Введите второе число:")))