from coffee_custom_exception import CoffeeException


class Coffee:
    def __init__(self, temperature):
        self.temperature = temperature

    def drink_coffee(self):
        if self.temperature < 4:
            raise CoffeeException("Coffee too Cold.")
        elif self.temperature > 20:
            raise CoffeeException("Coffee too Hot.")
        else:
            return "Coffee is good."


coffee = Coffee(3)
try:
    message = coffee.drink_coffee()
    print(message)
except CoffeeException as e:
    print(f"Exception Message : {e}")
