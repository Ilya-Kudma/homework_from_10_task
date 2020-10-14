def decorator(fun):
    def wrapping(*args):
        fun(*args[::-1])
    print('Changed args')

    return wrapping


@decorator
def reversed_arg(arg1, arg2):
    return print(f'{arg2} {arg1}  ==>  {arg1} {arg2}')


reversed_arg(1000, 2)