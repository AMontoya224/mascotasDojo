from mascota import Mascota

class Panda(Mascota):
    def __init__(self, name, tipo):
        super().__init__(name, tipo)
        pass

    def comer(self, golosinas):
        if golosinas == "bambu" or golosinas == "hojas" or golosinas == "fruta":
            self.energia += 5
            self.salud += 10
        else:
            print("No como eso!!!")
            
        return self