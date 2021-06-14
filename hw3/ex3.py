def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    return sum(sorted(my_list)[1:])

print(my_func(1, 2, 3))