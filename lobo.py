from mascota import Mascota

class Lobo(Mascota):
    def __init__(self, name, tipo):
        super().__init__(name, tipo)
        pass

    def comer(self, golosinas):
        if golosinas == "carne" or golosinas == "pollo" or golosinas == "cordero":
            self.energia += 5
            self.salud += 10
        else:
            print("No como eso!!!")

        return self