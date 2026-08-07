#index value
people=["Happy","Tony","Peter","Pepper","May","Ned"]
print(people)

print(len(people))
print(people[2])
print(people[-5])
print(people[1:4])

people.append("Jean")
print(people)
people.remove("Pepper")
print(people)
people.sort()
print(people)
people.reverse()
print(people)


#key value pair
teacher={"name":"Mr. Banner", "subject":"Physics","Experience":"10 years"}
print(teacher)
print(teacher["name"])
print(teacher["subject"])
teacher["Experience"]=12
print(teacher["Experience"])
print(teacher.get("Experience","Not found"))
print(teacher.get("email","Not found"))
teacher["email"]="brucebanner@gmail.com"
print(teacher.get("email","Not found"))
print(teacher)

#zip
num=[1,2,3,4,5,6]
people=["Happy","Tony","Peter","Pepper","May","Ned"]
dictonary=dict(zip(num,people))
print(dictonary)
print(dictonary[2])