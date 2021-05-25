###############################
# Valor a ingresar: ' AnA '
# Esta prueba unitaria sirve para verificar si el programa al recibir espacios (al inicio o al final del string) 
# sigue funcionando correctamente.
################################
import unittest
import ejercicio1

class UnitTest3(unittest.TestCase):
    def test_polindrome(self):
        self.assertEqual(ejercicio1.input_text, ejercicio1.input_text[::-1])

if __name__ == "__main__":
    output_UT3 = 'outputUT3.txt'
    with open(output_UT3, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)