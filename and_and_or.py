n=int(input("Enter a number:"))
print("Binary no:",bin(n)[2:])

print(12&10)
print(12|10)

print("Left shift of no.:",n<<1)
print("Right shift of no.:",n>>1)

print("NOT of no.:",~n)

print("XOR of no. with 12:",n^12)


for n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
    if n&1:
        print(n, "Odd")
    else:
        print(n, "Even")


n=int(input("Enter a no.:"))
a=n
while a>0:
    print(bin(a)[2:],"Last digit:",a&1)
    a>>=1
print("no of 1 in no.:",bin(n).count("1"))