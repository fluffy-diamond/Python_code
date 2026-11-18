#binary of 5,0,4
print(bin(5)[2:])
print(bin(0)[2:])
print(bin(4)[2:])

#XOR tests with random numbers 
#XOR cancels out pairs (x cancel out same number that appear 3 times)=>cancel out 2 and leave one
print(5^0)
print(5^5)
print(5^4)

#input a value to XOR
n=int(input("Enter a no. to XOR: "))

#XOR 3^n^3
print("with 3&3:",n^3^3)

#XOR 1^2^3^n^1^3^4^2
num=[1,2,3,n,1,3,4,2]
a=0
for i in num:
    a^=i
print("with",num,":",a)

#XOR 1^2^3^1^3^3^4^2
print(1^2^3^1^3^3^4^2, bin(1^2^3^1^3^3^4^2)[2:])


#split into 2 groups (Group A-can be flipped; Group B-cannot be flipped)

if n&1: #use and to decide if the number can be flipped
    print(bin(n)[2:],"bit 0 ON-group A") # the number can be flipped

else: #if cannot be flipped
    print(bin(n)[2:],"bit 0 OFF-group B") # the number cannot be flipped 