# test_calculadora.py
import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        # Aquí le decimos a la computadora: "Verifica que sumar 2 + 2 sea exactamente igual a 4"
        self.assertEqual(sumar(2, 2), 4)

if __name__ == '__main__':
    unittest.main()