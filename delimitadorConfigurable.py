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

    def test_multiples_numeros_retorna_la_suma(self):
        self.assertEqual(sumar("1,2,3"), 6)
        
    def test_muchos_numeros_retorna_la_suma(self):
        self.assertEqual(sumar("1,2,3,5,8,13"), 32)
        
    def test_admite_nuevas_lineas_como_separador(self):
        self.assertEqual(sumar("1,2,4\n5,6"), 18)
        
    def test_soporta_delimitador_personalizado_punto_y_coma(self):
        self.assertEqual(sumar("//;\n1;3;6;4"), 14)
        
    def test_soporta_delimitador_personalizado_pipe(self):
        self.assertEqual(sumar("//|\n1|3|6|4"), 14)

if __name__ == '__main__':
    unittest.main()