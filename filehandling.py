file=open("filehandling.txt","w")
file.write("Hello!\n")
file.write("My name is Heer\n")
file.close()

file=open("filehandling.txt","r")
content=file.read()
print(content)
file.close()

file=open("filehandling.txt","a")
file.write("I like to play basketball\n")
file.close()

file=open("filehandling.txt","r")
content=file.read()
print(content)
file.close()

file=open("filehandling.txt","r")
content=file.readlines()
print(len(content))