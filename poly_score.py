class basketball:
    def __init__(self, player, score):
        self.__player=player
        self.__score=score
    def info(self):
        print("The score for",self.__player,"is",self.__score)
    def hit(self):
        print(self.__player,"has scoared a three pointer")
    def getscore(self):
        return self.__score
    def newscore(self,ns):
        self.__score+=ns
        print("New score is",self.__score)

class football:
    def __init__(self, player, score):
        self.__player=player
        self.__score=score
    def info(self):
        print("The score for",self.__player,"is",self.__score)
    def hit(self):
        print(self.__player,"has scoared a goal")
    def getscore(self):
        return self.__score
    def newscore(self,ns):
        self.__score+=ns
        print("New score is",self.__score)

b=basketball("Peter",10)
f=football("Happy",1)

b.info()
b.hit()
b.getscore()
b.newscore(3)

print(" ")

f.info()
f.hit()
f.getscore()
f.newscore(2)

print(" ")

for sport in (b,f):
    sport.info()
    sport.hit()

print(" ")

new=int(input("Enter the new amount of points just scored for Basketball:"))
b.newscore(new)

print(" ")

new1=int(input("Enter the new amount of points just scored for Football:"))
f.newscore(new1)