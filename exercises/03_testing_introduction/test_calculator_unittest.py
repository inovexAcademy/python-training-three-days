import unittest
from codes.calculator import Calculator

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Setup TestCalculator class resources")

    def setUp(self) -> None:
        print("Setting up a fresh Calculator instance for a test")
        pass

    def test_calculator_name(self) -> None:
        """Test that the Calculator name is set correctly."""
        pass

    def test_add(self) -> None:
        """Test addition functionality."""
        pass

    def test_subtract(self) -> None:
        """Test subtraction functionality."""
        pass

    def test_multiply(self) -> None:
        """Test multiplication functionality."""
        pass

    def test_divide(self) -> None:
        """Test division functionality."""
        pass

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            pass

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestCalculator class resources")
