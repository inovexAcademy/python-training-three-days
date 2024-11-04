from typing import Union

import pytest
from error_handling import divide_numbers, InvalidInputError


# 1. Test Case: Valid division, use pytest parametrize
def test_valid_division(numerator: Union[int, float], denominator: Union[int, float],
                        expected_result: Union[int, float]) -> None:
    pass


# 2. Test Case: Division by zero, which should raise ZeroDivisionError
def test_division_by_zero() -> None:
    pass


# 3. Test Case: Non-numeric numerator, which should raise InvalidInputError
def test_non_numeric_numerator() -> None:
    pass


# 4. Test Case: Non-numeric denominator, which should raise InvalidInputError
def test_non_numeric_denominator() -> None:
    pass


# 5. Test Case: Both numerator and denominator are non-numeric, should raise InvalidInputError
def test_both_non_numeric() -> None:
    pass
