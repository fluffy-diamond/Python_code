n=4

total=n*(n+1)//2
print(total,"steps:1")

total1=0
for a in range(1,n+1):
    total1+=a
print(total1,"steps:",n)

total2=0
steps=0
for b in range(1,n+1):
    for c in range(1,b+1):
        total2+=1
        steps+=1
print(total2,"steps:",steps)


for d in [10,100,1000]:
    print(d*(d+1)//2)


n=4
points=list(range(1,n+1))
print(points,len(points))

for k in [92,39272,263920,1000000]:
    print(f"n={k:<5}, memory:{k:>5}")