import numpy as np
a = [1,2,3]
a.append([4,5])
print(a)
b = [1,2,3]
b.extend([4,5])
print(b)

c = np.append([1,2,3],[[4,5,6],[7,8,9]])
print(c)
d = np.append([[1,2,3],[4,5,6]],[[7,8,9]],axis = 0)
print(d)
