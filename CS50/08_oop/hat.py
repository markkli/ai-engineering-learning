import random

class Hat():
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} has been sorted into {house}.")

Hat.sort("Harry")