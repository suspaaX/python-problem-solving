#single inheritence



class Animal:

    def __init__(self,name,species):
        self.name=name
        self.species=species
        

    def makesound(self):
        print("make some sound")
        

class Dog(Animal):

    def __init__(self,breed):
        self.breed=breed

    def voice(self):
        print("brak")


dog1 = Animal("dog","dobber")


dog1.makesound()



