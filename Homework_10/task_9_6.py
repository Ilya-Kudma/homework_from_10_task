# Написать декоратор, который будет выводить время выполнения функции
from datetime import datetime
from typing import List
from functools import reduce


def my_decorator(func):

    def time_result_my_summa(numbers):
        time1 = datetime.now()
        func(numbers)
        time2 = datetime.now()
        result_time = time2 - time1
        return print(result_time)

    return time_result_my_summa


@my_decorator
def my_summa(numbers: List[int]):
    """
    :param numbers: List[int]
    :return: summa_values
    """
    summa_values = reduce(lambda a, b: a + b, numbers, 0)
    print(summa_values)
    return summa_values


my_summa([1, 2, 3])
