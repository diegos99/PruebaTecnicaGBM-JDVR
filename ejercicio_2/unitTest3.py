###############################
# Valor a ingresar: número entero positivo. (representa el numero de sistema de puntuación)
# Esta prueba unitaria verifica si el No. de sistema de puntuación a consultar es valido o no.
# Tomando en cuenta que existen 2 sistemas de puntuación (1 y 2), si es mayor que 2 es invalido.
################################
import unittest
import ejercicio2

class UnitTest3(unittest.TestCase):
    def test_sistema_puntaje(self):
        self.assertTrue(ejercicio2.ResultadosSP12(1))

if __name__ == "__main__":
    output_UT3 = 'outputUT3.txt'
    with open(output_UT3, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)