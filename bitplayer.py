print(bin(5)[2:])
print(5|2, bin(5|2)[2:])

print(bin(7)[2:])
print(7&5, bin(7&5)[2:])

n=int(input("Enter a random no.:"))
if n>0 and (n & (n-1))==0:
    print (bin(n)[2:], "is a power of 2")
else:
    print (bin(n)[2:], "is not a power of 2")

n=int(input("Enter a no.:"))
a=n
p=0
while a>0:
    print(bin(a)[2:],"Last digit:",a&1)
    if a&1:
        break
    a>>=1
    p+=1
print("first 1 in no.",n,"is at position",p)




for i in range(5):
    mask=1<<i
    print(i, mask, bin(mask)[2:])

n=int(input("Enter a random no.:"))
a=(n>>2)&1
if a:
    print(n, bin(n)[2:],"bit 2 is on")
else:
    print(n, bin(n)[2:],"bit 2 is off")