class Duck:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def walk(self):
        print(f"{self.name} is walking.")

    def eat(self):
        print(f"{self.name} is eating {self.food}.")
