from animal_parent import Animal


class Cat(Animal):
    def __init__(self, color):
        Animal.__init__(self, color)
        self.color = color

    def speak(self):
        print(f"{self.color} cat make a big sound.")


cat = Cat(color="White Color")
cat.speak()

