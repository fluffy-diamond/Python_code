num=int(input("Enter a number(preferably large):"))
p=2
prime=[True for i in range(num+1)]
while (p*p<=num):
    if (prime[p]==True):
        for i in range(p*p,num+1,p):
            prime[i]=False
    p+=1
for p in range(2,num+1):
    if prime[p]:
        print("Prime no. in range provided are:",p)


from math import sqrt
no=int(input("Enter a no.:"))
if no>1:
    for i in range(2,int(sqrt(no))):
        if (no%i)==0:
            print("Not prime no.")
    else:
        print("It is a prime no.")
else:
    print("Not prime no.")


number=int(input("Enter a number:"))
for i in range(1,number+1):
    c=0
    rev=0
    abc=number
    for k in range(1,abc+1):
        if abc%k==0:
            c+=1
    if c==2:
        while abc>0:
            rev=rev*10+(abc%10)
            abc//=10
        if rev==number:
            print("It is a palindrome")
            break
        else:
            print("Not a palindrome")
            break