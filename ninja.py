from lobo import Lobo
from panda import Panda

class Ninja:
    def __init__(self, nombre, apellidos, mascota, especie):
        self.nombre = nombre
        self.apellidos = apellidos
        self.especie = especie.lower()
        if especie == "lobo":
            self.mascota = Lobo(mascota, especie)
        else:
            self.mascota = Panda(mascota, especie)
    
    def caminar(self):
        print("Sacaré a " + self.mascota.name + " para pasear")
        self.mascota.jugar()
        return self
    
    def alimentar(self, comida):
        print("Daré de comer a " + self.mascota.name)
        self.mascota.comer(comida)
        return self
    
    def bañar(self):
        print("Bañaré a " + self.mascota.name)
        self.mascota.ruido()
        return self
    
    def informacion_ninja(self):
        print("Nombre: " + self.nombre + " " + self.apellidos + ", tiene un " + self.especie)
        self.mascota.informacion()
        return self