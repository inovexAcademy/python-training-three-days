import pytest
from codes.calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    """Fixture to initialize Calculator instance with a name."""
    pass

def test_calculator_name(calculator) -> None:
    """Test that the Calculator name is set correctly."""
    pass

def test_add(calculator) -> None:
    """Test addition functionality."""
    pass

def test_subtract(calculator) -> None:
    """Test subtraction functionality."""
    pass

def test_multiply(calculator) -> None:
    """Test multiplication functionality."""
    pass

def test_divide(calculator) -> None:
    """Test division functionality."""
    pass

def test_divide_by_zero(calculator) -> None:
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        pass
