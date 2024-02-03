import unittest
from your_module_name import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -5, 3.5, -2]), 3.5)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_string_values(self):
        with self.assertRaises(TypeError):
            max_integer(["abc", "def", "ghi"])
