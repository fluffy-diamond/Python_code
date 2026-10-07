number=int(input("Enter a number:"))
digits=len(str(number))

num=0
no=number

while no>0:
    a=no%10
    num +=a**digits
    no//=10

if number==num:
    print("Armstrong no.")
else:
    print("Not Armstrong no.")






number=int(input("Enter a no."))

for i in range(1,number+1):
    if number%i==0:
        print(i,"is a factor of",number)







def a(b):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    value=0
    for i in range(0,len(b)-1):
        if roman[b[i]]>roman[b[i+1]]:
            value+=roman[b[i]]
        else:
            value-=roman[b[i]]
    return value+roman[b[-1]]

roman=input("Input a roman number:")

print(a(roman))