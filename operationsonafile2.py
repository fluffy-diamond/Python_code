import os

if os.path.exists("test"):
    os.rmdir("test")

with open ("filehandling.txt","r") as file:
    for line in file:
        print(line.strip())

with open ("filehandling2.txt","r") as file:
    for line in file:
        word=line.split()
        print(len(word),"words:",line.strip())

if os.path.exists("allnotes.txt"):
    print("This file already exists")
    os.remove("allnotes.txt")
else:
    print("Creating file now")
    with open ("allnotes.txt","x") as file:
        pass
    content=""
    with open ("filehandling.txt","r") as file:
        content+=file.read()+"\n"
    with open ("filehandling2.txt","r") as file:
        content+=file.read()
    with open ("allnotes.txt","w") as file:
        file.write(content)
    with open ("allnotes.txt","r") as file:
        print(file.read())

