name="Heer"
age=15
height=1.6
female=True

print(type(name))
print(type(age))
print(type(height))
print(type(female))

#mathematical operation
price=10.5
quantity=10

print(price*quantity)

print("Is price less than $10?",price<10)
print("Is quantity greater than or equal to 10?",quantity >= 10)
print("Is price exactly 10.5?", price==10.5)


#strings
surname="Dholariya"
fullname = name +" "+ surname
print("My name is ", fullname)
print("No. of letters in my name ", len(fullname)-1)
print(fullname[3:6])

temp= name
name=surname
surname=temp
fullname = name +" "+ surname
print(print("My name is ", fullname))
