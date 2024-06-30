from PythonInheritance.singleinheritance.AnimalParent import Animal


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


dog1 = Dog(name="Bull Dog", color="white")
dog1.eat()
dog1.sleep()
print(dog1.is_alive)
