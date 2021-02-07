import numpy as np

list1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

list2 = np.array([
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])
dot1 = np.dot(list1, list2)
mul1 = np.matmul(list1, list2)
print(mul1)
print(mul1)

sum = list2.sum()
print(sum)

new = np.random.rand(5, 5)
# print(new)

new1 = np.arange(15, 55, 1).reshape(2, 20)
sz = new1.size

print(sz)
