import numpy as np
datatype=[("name","S15"),("grade",int),("height",float)]
studentdetails=[("Heer",10,1.64),("Betty",5,1.6),("Amy",8,1.61)]
students=np.array(studentdetails, dtype=datatype)
print(np.sort(students,order="height"))
print(np.sort(students,order="name"))
print(np.sort(students,order="grade"),"\n")




a=np.arange(1,10,dtype=np.float64).reshape(3,3)
print(a,"\n")

b=np.array([10,10,10])
print(b,"\n")

print(a+b,'\n')
print(a-b,'\n')
print(a*b,'\n')
print(a/b,'\n')




x=np.array([1,2,3,9,1,2,1])
y=np.array([4,5,6,9,1,3,1])
z=np.concatenate((x,y))
print(z)

c=np.where(z==1)
print(c,"\n")



from numpy import random
d=random.randint(1,7)
print(d)