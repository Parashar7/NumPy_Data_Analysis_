import numpy as np

# list1= np.array([33,44,55,54])

# list2 =np.array([1,44,55,6])

# ans=(list1==list2).sum()
# print(ans)

list3 = np.array([
    [[2, 3, 32, 34, 67],
     [43, 11, 3, 4, 78]],

    [[5, 77, 34, 6, 2],
     [22, 76, 87, 3, 9]],

    [[2, 3, 69, 4, 38],
     [45, 37, 81, 99, 18]]

])
ans = list3.shape
# print(ans)

array_index = list3[:2]
# print(array_index)

# random array

ran_array = np.random.rand(2, 3)
# print(ran_array)

# identity array
id = np.eye(3)
# print(id)

# a_range
# (start, end, step)
arr = np.arange(10, 90, 10)
# print(arr)

# equally spaced numbers in a array

num = np.linspace(3, 27, 15)
# print(num)

# reshape
new_array = np.arange(10, 90, 3).reshape(3, 9)
# shape= new_array.shape
print(new_array)
# print(shape)
