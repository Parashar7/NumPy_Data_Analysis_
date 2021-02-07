import numpy as np

list = np.arange(10, 21+1, 1)
sz= list.size
print(sz)
new_list = list.reshape(3, 4)
print(list)
print(new_list)


