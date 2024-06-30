from mammal import Mammal


class Dog(Mammal):
    def __init__(self, animal_name, color, breed):
        Mammal.__init__(self, animal_name, color)
        self.breed = breed

    def bark(self):
        print(f"{self.animal_name} is barking.")


dog = Dog("Tiger", "White", "Bulldog")
dog.eat()
dog.walk()
dog.bark()
print("Dog Color : ",dog.color)
print("Dog Breed : ",dog.breed)


