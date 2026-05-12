import unittest
from    string_calculator import sumar

class TestStringCalculator(unittest.TestCase):
    def test_string_vacio_retorna_cero(self):
        self.assertEqual(sumar(""), 0)

if __name__ == '__main__':
    unittest.main()