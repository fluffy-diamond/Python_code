class parrot:
    species ="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def paint(self, art):
        return  "{} paints {}".format(self.name,art)
    def play(self, sport):
        return "{} plays {}".format(self.name,sport)

happy=parrot("Happy",2)
daisy=parrot("Daisy",3)

print("{} is a {} and is {} years old".format(happy.name,happy.species,happy.age))
print("{} is a {} and is {} years old".format(daisy.name,daisy.species,daisy.age))
print(happy.paint("landscapes"))
print(daisy.play("basketball"))

