from animal import Animal

class Oiseaux(Animal):
     
    def __init__(self,weight,size,__altitude_max):
         super().__init__(weight,size)
         self.__altitude_max=__altitude_max
    
    def get_altitude_max(self):
        return self.__altitude_max
    
    def set_altitude_max(self,altitude_max):
        self.__altitude_max = altitude_max

    def se_deplacer(self):
        print("je vole")