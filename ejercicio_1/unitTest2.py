###############################
# Valor a ingresar: AnA
# Esta prueba unitaria demuestra que el programa es capaz de aceptar mayusculas y minusculas en el string, 
# si fallara, quiere decir que el programa no está haciendo el uso de una funcion lower().
################################
import unittest
import ejercicio1

class UnitTest2(unittest.TestCase):
    def test_polindrome(self):
        self.assertEqual(ejercicio1.input_text, ejercicio1.input_text[::-1])

if __name__ == "__main__":
    output_UT2 = 'outputUT2.txt'
    with open(output_UT2, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)