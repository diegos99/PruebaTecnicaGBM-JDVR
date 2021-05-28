###############################
# Esta prueba unitaria verifica si el valor máximo obtenido del array de puntajes finales se encuentra en dicho array.
################################
import unittest
import ejercicio2

class UnitTest5(unittest.TestCase):
    def test_longitud_registro_puntos(self):
        self.assertIn(max(ejercicio2.DeteccionGanador(1)), ejercicio2.DeteccionGanador(1))

if __name__ == "__main__":
    output_UT5 = 'outputUT5.txt'
    with open(output_UT5, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)