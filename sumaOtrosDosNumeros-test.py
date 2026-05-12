import unittest
from string_calculator import sumar

class TestStringCalculator(unittest.TestCase):
    
    def test_string_vacio_retorna_cero(self):
        self.assertEqual(sumar(""), 0)
        
    def test_un_numero_retorna_el_mismo_numero(self):
        self.assertEqual(sumar("1"), 1)
        
    def test_dos_numeros_retorna_la_suma(self):
        self.assertEqual(sumar("1,2"), 3)
        
    def test_otros_dos_numeros_retorna_la_suma(self):
        self.assertEqual(sumar("4,2"), 6)

if __name__ == '__main__':
    unittest.main()