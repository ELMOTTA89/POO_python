class zoo:
    def __init__(self, animals=[]):
        self.animals=animals

    def add_animal(self,animal):
        self.animals.append(animal)

   # def show_an(self):
   #     for ani in self.animals:
   #         print(ani.get_size())
   #          