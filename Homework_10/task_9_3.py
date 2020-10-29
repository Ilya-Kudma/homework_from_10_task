from typing import List
from functools import reduce


def my_decorator(func):

    def del_even_value(numbers):
        numbers = list(filter(lambda x: x % 2, numbers))
        result = func(numbers)
        return result

    return del_even_value


@my_decorator
def my_summa(numbers: List[int]):
    """
    :param numbers: List[int]
    :return: summa_values
    """
    summa_values = reduce(lambda a, b: a + b, numbers, 0)
    print(summa_values)
    return summa_values


my_summa([1, 2, 3, 4, 5, 7, 8])