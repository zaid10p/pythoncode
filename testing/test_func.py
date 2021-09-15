from testing.func import divide, multiply
from unittest import TestCase


class TestFunctions(TestCase):
    def test_divide_result(self):
        expected_result = 5.0
        self.assertAlmostEqual(divide(15, 3),
                               expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        expected_result = 0
        self.assertEqual(divide(0, 4), expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_negative(self):
        inputs = (3, -5, 0.5)
        expected = -7.5
        self.assertEqual(multiply(*inputs), expected)
