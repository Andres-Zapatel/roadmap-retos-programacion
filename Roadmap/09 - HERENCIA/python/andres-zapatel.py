"""
ejercicio
"""

# Superclase

class Animal:
    def __init__(self, nombre:str): 
        self.nombre = nombre

    def sonido(self):
        print("Este animal emite un sonido predeterminado!")

# Subclases

class Perro(Animal):

    def sonido(self):
        print("guau guau")

class Gato(Animal):

    def sonido(self):
        print("Meow Meow")

mi_animal = Animal("Animal Generico")
mi_animal.sonido()

mi_perro = Perro("Perro")
mi_perro.sonido()

mi_gato = Gato("Gato")
mi_gato.sonido()