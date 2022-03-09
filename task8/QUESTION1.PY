import numpy as np
x = np.array([10,11,12,13,14])
print(x)
y = 5
z = np.zeros(len(x) + (len(x)-1)*(y))
z[::y+1] = x
print(np.floor(z))
