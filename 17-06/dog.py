from animal import animal
class dog(animal):

    def __init__(self):
        print("child con !")

    def __init__(self,name,weight,colour):
        self.colour=colour
        super().__init__(name,weight)

    def abc(self):
        print("im from child class")

    def dog_details(self):
        super().greet ()
        print(f"{self.name}{self.colour}")

obj=dog("husky","7kg","white-black")