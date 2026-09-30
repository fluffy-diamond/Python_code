n=10

steps=1
print(steps)

steps=0
for k in range(n):
    steps+=1
print(steps)

steps=0
for k in range(n):
    for h in range(n):
        steps+=1
print(steps)



scores=[10,8,7,3,2,6,9,1,4,5]

print(scores)
no=int(input("Choose a random no. from 1-10:"))

steps=0
for k in scores:
    steps+=1
    if k==no:
        break
print(steps)


if steps==1:
    print("you have the best case")
elif steps==10:
    print("you have worst case")
else:
    print("you have mid  case")


n=int(input("Enter a random no pls:"))

for i in range(n):
    pass
print(n)

for i in range(n):
    for j in range(n):
        pass
print(n*n)