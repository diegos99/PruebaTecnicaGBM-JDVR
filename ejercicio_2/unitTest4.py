###############################
# Esta prueba unitaria verifica si la longitud de puntos registrados concuerda con el No. de pilotos en la temporada.
################################
import unittest
import ejercicio2

class UnitTest4(unittest.TestCase):
    def test_longitud_registro_puntos(self):
        self.assertEqual(len(ejercicio2.puntos_por_carrera), 15)

if __name__ == "__main__":
    output_UT4 = 'outputUT4.txt'
    with open(output_UT4, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)