from animal import Animal

class zoo:
    def __init__(self, animals=[]):
        self.animals=animals

    def add_animal(self,animal:Animal):
        self.animals.append(animal)

    def show_an(self):
        for ani in self.animals:
            print(type(ani))
            ani.__str__(ani)
             