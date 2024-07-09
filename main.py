from animal import Animal
from Oiseaux import Oiseaux
from serpent import serpent
from zoo import zoo

###### Main #####
#creer un environement conda
#conda create --name $ENVIRONMENT_NAME python tensorflow

if __name__=="__main__":
     
    A1=Animal(18,15)
    S1=serpent(1,2)
    O1=Oiseaux(100,200,300)
    Z1=zoo([O1,S1])
    Z2=zoo([O1,S1,O1])

    print("size=",A1.get_size())
    print("wieght=",A1.get_weight())
     
    O1.se_deplacer()
    S1.se_deplacer()

    print("size=",O1.get_size())
    print("wieght=",O1.get_weight())
    print("altitude=",O1.get_altitude_max())
    #O1.set_size(-2)
    Z1.add_animal(S1)
    Z1.show_an()
    Z3 = Z1 + Z2
    print(type(Z3))
    Z3.show_an()
    



     

