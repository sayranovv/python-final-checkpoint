import unittest

from main import UglyNumbersGenerator

class TestUglyNumbersGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = UglyNumbersGenerator()

    def test_first_elements(self):
        self.assertEqual(self.gen.get_numbers(1), [1])
        self.assertEqual(self.gen.get_numbers(2), [1, 2])
        self.assertEqual(self.gen.get_numbers(5), [1, 2, 3, 4, 5])
        self.assertEqual(self.gen.get_numbers(10), [1, 2, 3, 4, 5, 6, 8, 9, 10, 12])

    def test_no_duplicates(self):
        nums = self.gen.get_numbers(20)
        self.assertEqual(len(nums), len(set(nums)))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.gen.get_numbers(0)
        with self.assertRaises(ValueError):
            self.gen.get_numbers(-5)
        with self.assertRaises(ValueError):
            self.gen.get_numbers(3.14)
        with self.assertRaises(ValueError):
            self.gen.get_numbers("ten")

if __name__ == "__main__":
    unittest.main()