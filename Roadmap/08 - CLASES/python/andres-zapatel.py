"""
CLASES
"""
"""
ejercicio
"""

class Programador:
    def __init__(self, nombre:str, edad:int, lenguaje:list): #nombre, edad y lenguaje son parametros
        self.nombre = nombre
        self.edad = edad
        self.lenguaje = lenguaje

    def print(self):
        print( f"Hola, soy {self.nombre}, tengo {self.edad} años y programo en {self.lenguaje}." )

mi_Programador = Programador("Andrés Zapatel", 25, ["Python"])
mi_Programador.print()

mi_Programador.edad = 33
mi_Programador.print()