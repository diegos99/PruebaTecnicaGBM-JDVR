###############################
# Valor a ingresar: número entero positivo.
# Esta prueba unitaria verifica si el sistema de puntuación 1 realiza correctamente la asignación de puntos 
# según el puesto obtenido en la carrera.
# Tomando en cuenta que el Sistema de puntaje 1 se encuentra estructurado de esta manera:
# Lugares-->  1,2,3,4,5,6,7,8 
# Punteos--> 10,8,6,5,4,3,2,1
################################
import unittest
import ejercicio2

class UnitTest1(unittest.TestCase):
    def test_puntaje1(self):
        self.assertEqual(ejercicio2.AsignarPunteoSP1(8), 1)

if __name__ == "__main__":
    output_UT1 = 'outputUT1.txt'
    with open(output_UT1, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)