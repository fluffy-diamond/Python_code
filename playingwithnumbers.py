number=int(input("Enter a number:"))

num=number
newnumber=0

while num>0:
    a=num%10
    newnumber=newnumber*10+a
    num//=10

if number==newnumber:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")





numlarge=int(input("Enter a larger no.:"))
numsmall=int(input("Enter a smaller no.:"))

multiple=numlarge*numsmall

while(numsmall):
    store=numsmall
    numsmall=numlarge%numsmall
    numlarge=store

lcm=int(multiple/numlarge)

print("HCF:",numlarge)
print("LCM:",lcm)



