import numpy as np
x=input("Enter The First Array :").split()
x=np.array(list(map(int,x)))
y=input("Enter The Second Array :").split()
y=np.array(list(map(int,y)))
comparison = (x == y)
Condition= comparison.all()
if(Condition is True):
    print(True)
else:
    print(False)
