import numpy as np
datatype=[("name","S15"),("grade",int),("height",float)]
studentdetails=[("Heer",10,1.64),("Betty",5,1.6),("Amy",8,1.61)]
students=np.array(studentdetails, dtype=datatype)
print(np.sort(students,order="height"))
print(np.sort(students,order="name"))
print(np.sort(students,order="grade"))