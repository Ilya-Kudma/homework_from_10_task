# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
# example_1
from functools import reduce
list_1 = [3, 2, 3, 5, 6]
print(reduce(lambda x, y: x * y if y % 3 == 0 and y != 0 else x * 1, list_1))

# example_2
my_list = [2, 3, 0, 5, 6]

filtered_list = list(filter(lambda x: not x % 3, my_list))

print(reduce(lambda first_number, second_number: first_number * second_number, filtered_list))