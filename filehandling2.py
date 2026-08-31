file=open("filehandling2.txt","x")
file.close()

file=open("filehandling2.txt","w")
file.write("Hello!\n")
file.write("I have just created a new txt file using python!\n")
file.close()

file=open("filehandling2.txt","r")
print(file.read)
file.close()

file=open("filehandling2.txt","a")
file.write("It can do the same things as the first file but this one just creates the file automatically!")
file.close()

file=open("filehandling2.txt","r")
print(file.read())
file.close()

file=open("filehandling2.txt","r")
print(len(file.readlines()))
file.close()