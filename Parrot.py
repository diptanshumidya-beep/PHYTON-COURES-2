class Parrot:

    species = "bird"

    def __init__(self,name,age):
        self.name = name

        if age < 0 :
            age = 0
        self.age = age 


parrot_name = input("Name of first paroot ?")


blu = Parrot(parrot_name,10)

woo = Parrot("wOO",15)

print ( blu.name , "is a" , blu.species)

print ("WOO is a " , Parrot.species)


print(blu.name , "is" , blu.age , "YERAS OLD")

print(woo.name , "is" , woo.age , "years old")


ghost = Parrot("Ghooosti yay" , -3)

print(ghost.name , "is" , ghost.age , "yeras oldi")