import unittest
from age_printer import print_age

class TestAgePrinter(unittest.TestCase):
    def test_print_age(self):
        self.assertEqual(print_age(15), "Your age is 15")
        self.assertEqual(print_age(16), "Your age is 16")
        self.assertEqual(print_age(20), "Your age is 20")

if __name__ == '__main__':
    unittest.main()