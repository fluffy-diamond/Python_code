def intro(name):
    print("Hello,",name,"!")
username=input("Enter your name:")
intro(username)

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)




num=int(input("Enter a number:"))

if num==0:
    print("The factorial is 1.")
elif num<0:
    print("There is no factorial.")
else:
    print("The factorial is",fact(num))




def add():
    return x+y
def minus():
    return x-y
def multi():
    return x*y
def divide():
    return x//y

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))

print("The sum is:",add())
print("The difference is:",minus())
print("The product is:",multi())
print("The quotient is:",divide())