class PartyAnimal: #defines new class = provides blueprint "PartyAnimal" to create the object

    def __init__(self): #Constructor.(Method _init_) Creates an object and sets the variable of the object to 0
        self.x = 0
    def party(self): #Creates a method that adds +1 to object variable and prints something 
        self.x = self.x +1
        print("So far", self.x)
    

# Stuff I can do with it 
pt = PartyAnimal() #creates an object PartyAnimal() with attribute x=0 and the "party()" method
pt.party()  #invokes the party() method
pt.party()    

#Info about the variable
print(type(pt))
print(dir(pt))
print(type(pt.x))
print(type(pt.party))
s = PartyAnimal()
s.party()
print(s.x, pt.x)
