from animal import Animal

class serpent(Animal):
     
     def __init__(self,weight,size):
         super().__init__(weight,size)

     def se_deplacer(self):
        print("je rampe")