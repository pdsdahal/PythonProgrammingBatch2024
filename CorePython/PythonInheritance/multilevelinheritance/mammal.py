from animal import Animal


class Mammal(Animal):
    def __init__(self, animal_name, color):
        Animal.__init__(self,animal_name)
        self.color = color

    def walk(self):
        print(f"{self.animal_name} is walking.")
