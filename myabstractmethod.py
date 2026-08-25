from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat

    def display(self):
        print(self.name,self.habitat)

    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def __init__(self, name, habitat,breed):
        super().__init__(name, habitat)
        self.breed=breed
    def sound(self):
        print(self.breed,". A dog says woof.")

class bird(animal):
    def __init__(self, name, habitat,breed):
            super().__init__(name, habitat)
            self.breed=breed
    def sound(self):
        print(self.breed,". A bird says tweet.")


class cow(animal):
    def __init__(self, name, habitat,breed):
            super().__init__(name, habitat)
            self.breed=breed
    def sound(self):
        print(self.breed,". A cow says moo.")



d=dog("Happy","House","Golden Retriever")
b=bird("Peggy","sky","parrot")
c=cow("Agatha","grasslands","brown cow")

for a in [d,b,c]:
     a.sound()
     a.display()