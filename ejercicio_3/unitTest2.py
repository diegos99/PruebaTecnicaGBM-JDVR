###############################
# Valor a ingresar: número 0.
# Esta prueba unitaria verifica si el las variable k e y son iguales a 0
################################
import unittest
import ejercicio3

class UnitTest2(unittest.TestCase):
    def test_cero(self):
        self.assertTrue(ejercicio3.k == 0 and ejercicio3.y == 0)

if __name__ == "__main__":
    output_UT2 = 'outputUT2.txt'
    with open(output_UT2, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)