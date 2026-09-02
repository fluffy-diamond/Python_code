file=open("filehandling.txt","r")
x=int(input("Characters you want to read from the file:"))
print(file.read(x))
file.close()

file=open("filehandling.txt","r")
lines=file.readlines()
print(len(lines))
for k in range(len(lines)):
    print(k+1,lines[k].strip())
file.close()

file=open("filehandling.txt","r")
word=input("Skip lines starting with word:")
for line in file:
    if line.startswith(word):
        print("skip:",line.strip())
    else:
        print("keep:",line.strip())
file.close()

file=open("filehandling.txt","r")
for i in range(0,len(lines),2):
    print(lines[i])
file.close()