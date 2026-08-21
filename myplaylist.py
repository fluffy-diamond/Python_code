class playlist:
    def __init__(self, name,type):
        self.name= name
        self.type= type
        self.mysongs=[]

    def add(self,song):
        self.mysongs.append(song)

    def delete(self,song):
        self.mysongs.remove(song)

    def display(self):
        print(mysongs)


myplaylist=playlist("roadtripsongs","pop")

while True:
    print("1:Add song / 2:Delete song / 3:Display playlist / 4:Exit")
    choice= input("Your choice:") 

    if choice=="1":
        song= input("Enter a song to add:")
        myplaylist.add(song)
    elif choice=="2":
        song=input("Enter a song to remove:")
        myplaylist.delete(song)
    elif choice=="3":
        myplaylist.display()
        del myplaylist
        break
    else:
       print("Choose 1/2/3/4 only!")