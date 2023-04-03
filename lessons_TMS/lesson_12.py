from functools import wraps
from typing import Any, Callable

# def check_int(func: Callable) -> Callable:
#     @wraps(func)
#     def inner(num: int) -> Any:
#         if type(num) != int:
#             print('ввели некорректные данные')
#             return
#         return print('ok')
#     return inner
#
# @check_int
# def is_even(num) ->bool | None:
#     return num % 2 == 0

# is_even('sfvv')
# is_even('2')
# is_even(4)
# is_even(5)

# is_even = check_int(is_even)

class check_int:
    def __init__(self, func):
        self.func = func

    def __call__(self, num: int):
        if type(num) != int:
            print('ввели некорректные данные')
            return
        return print('ok')


@check_int
def is_even(num) ->bool | None:
    return num % 2 == 0

is_even('sfvv')
is_even('2')
is_even(4)
is_even(5)



