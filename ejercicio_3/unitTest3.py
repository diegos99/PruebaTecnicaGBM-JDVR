###############################
# Valor a ingresar: número 0.
# Esta prueba unitaria verifica si el las variable k e y son variables de tipo interger
################################
import unittest
import ejercicio3

class UnitTest3(unittest.TestCase):
    def test_entero(self):
        self.assertTrue(type(ejercicio3.k) == int and type(ejercicio3.y) == int)

if __name__ == "__main__":
    output_UT3 = 'outputUT3.txt'
    with open(output_UT3, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)