###############################
# Valor a ingresar: dad
# Esta prueba unitaria es satisfactoria si la palabra ingresada es políndroma.
################################
import unittest
import ejercicio1

class UnitTest1(unittest.TestCase):
    def test_polindrome(self):
        self.assertEqual(ejercicio1.input_text, ejercicio1.input_text[::-1])

if __name__ == "__main__":
    output_UT1 = 'outputUT1.txt'
    with open(output_UT1, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)