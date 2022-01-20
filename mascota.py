class Mascota:
    def __init__(self, name , tipo):
        self.name = name
        self.tipo = tipo
        self.energia = 0
        self.salud = 0
    
    def dormir(self):
        self.energia += 25

    #def comer(self, comida):
        #if super().alimento(comida):
    #    self.energia += 5
    #    self.salud += 10
    
    def jugar(self):
        self.salud += 5
    
    def ruido(self):
        print("Rggg!!! (sonido de " + self.name + ")")
    
    def informacion(self):
        print(self.name + " tiene Vida: " + str(self.salud) + ", Energía: " + str(self.energia))
        print("")
