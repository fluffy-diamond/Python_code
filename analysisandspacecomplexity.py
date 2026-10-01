score=[1,3,5,7,9,11,13,15,17]
print(score)
no=int(input("Choose one no. from above:"))

steps=0
low=1
high=len(score)

while low<=high:
    mid=(low+high)//2
    steps+=1
    if score[mid]==no:
        break
    elif score[mid]>no:
        high=mid-1
    else:
        low=mid+1
print("Your no. is:",no,"steps:",steps,"position:",mid+1)


n=int(input("Enter a no.:"))

def abc(num):
    print(num)
    if num>0:
        abc(num-1)
abc(n)
print("steps:",n+1)

for size in [10,20,30]:
    print(size,"steps for each:",size+1)


for n in [10,100,1000]:
    print(n,n*n)
    