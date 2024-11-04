from datetime import datetime
from typing import Callable, Any
from functools import wraps

def logger_decorator(print_time: bool = True) -> Callable:
    pass


@logger_decorator(print_time=True)
def add_numbers(a: int, b: int) -> int:
    return a + b

@logger_decorator(print_time=False)
def multiply_numbers(a: int, b: int) -> int:
    return a * b
