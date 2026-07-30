num =int(input( "Enter a number for multiplication:"))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")



num2=int(input("Enter a new number for a patttern:"))

for i in range(1,num2+1):
    for j in range(i):
        print("#",end=" ")
    print()



num3=int(input("Enter a newer number to check if it's prime or not:"))

if num>1:
    for i in range(2,int(num3//2)+1):
        if num % i==0:
            print("It is not a prime number.")
            break
    else:
        print("It is a prime number")
else:
    print("It is not a prime number.")



totalsum=0
num4=1
while num4<=10:
    totalsum += num4
    num4 += 1
print(totalsum)

