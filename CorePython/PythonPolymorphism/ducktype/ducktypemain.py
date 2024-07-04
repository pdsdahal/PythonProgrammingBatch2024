from duck import Duck
from chicken import Chicken


def duck_chicken(bird):
    bird.walk()


duck1 = Duck(name="Daffy", food="maize")
chicken1 = Chicken(name="Boiler", food="wheat")

duck_chicken(duck1)
duck_chicken(chicken1)
