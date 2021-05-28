###############################
# Valor a ingresar: número entero positivo.
# Esta prueba unitaria verifica si el sistema de puntuación 2 realiza correctamente la asignación de puntos 
# según el puesto obtenido en la carrera.
# Tomando en cuenta que el Sistema de puntaje 2 se encuentra estructurado de esta manera:
# Lugares-->  1, 2, 3, 4, 5,6,7,8,9,10 
# Punteos--> 25,18,15,12,10,8,6,4,2,1
################################
import unittest
import ejercicio2

class UnitTest2(unittest.TestCase):
    def test_puntaje2(self):
        self.assertEqual(ejercicio2.AsignarPunteoSP2(1), 25)

if __name__ == "__main__":
    output_UT2 = 'outputUT2.txt'
    with open(output_UT2, "w") as file:
        result = unittest.TextTestRunner(file)
        unittest.main(testRunner=result)