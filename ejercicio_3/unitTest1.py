###############################
# Valor a ingresar: número entero positivo.
# Esta prueba unitaria verifica si el la variable t se encuentra en el rango de 1 a 1000 
################################
import unittest
import ejercicio3

class UnitTest1(unittest.TestCase):
    def test_rango(self):
        self.assertTrue(ejercicio3.t>=1 and ejercicio3.t<=1000)

if __name__ == "__main__":
    output_UT1 = 'outputUT1.txt'
    with open(output_UT1, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)