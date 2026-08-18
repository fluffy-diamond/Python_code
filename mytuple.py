food=("pasta","sandwitch","salad","curry")
food1=("roti","dhokala","thepla","jalebi")
print(food[0])
print(food[1])
print(food[-1])
print(food[-2])

allfood=(food,food1)
print(allfood)
print(allfood[0][1])
print(allfood[1][3])

for detail in food:
    print("-",detail)

sandwitch={"bread","tomato","ketchup","onion","bread","lettuce"}
biryani={"rice","tomato","onion","peas","rice"}
print(sandwitch)
print(biryani)
sandwitch.add("cucumbur")
print(sandwitch)

print(sandwitch.intersection(biryani))
print(sandwitch.union(biryani))
print(sandwitch.difference(biryani))
print(sandwitch.symmetric_difference(biryani))