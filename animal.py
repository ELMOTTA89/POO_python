class Animal:

    def __init__(self,weight,size):
          self.__weight=weight
          self.__size=size

    def se_deplacer(self):
        pass

    def get_size(self):
        return self.__size
    
    def get_weight(self):
        return self.__weight
    
    def set_size(self,size):

        if size < 0:
            raise ValueError("le  poids ne peut pas etre negatif")
        else:
            self.__size = size
    
    def set_weight(self,weight):
        if weight < 0:
            raise ValueError("la taille ne peut pas etre negative")
        else:
            self.__weight=weight
    
    def __str__(self,animal) -> str:
        print(animal.get_size())
        print(animal.get_weight())
    