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