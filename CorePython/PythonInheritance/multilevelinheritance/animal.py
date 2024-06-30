class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def eat(self):
        print(f"{self.animal_name} is eating.")