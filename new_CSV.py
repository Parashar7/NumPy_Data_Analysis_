import numpy as np

phdata = np.genfromtxt('phvalue.txt', delimiter=' ', skip_header=1)

print(phdata)
shape_value = phdata.shape
print(shape_value)
#new_array = phdata.reshape(2132, 3, 3)
#print(new_array)
#new_array1= np.round(new_array)
#index_value = new_array[132]
#print(index_value)
#index_value1 = index_value[2, 1]

#print(index_value1)
#sliceing

#sliced_array= new_array1[2128:2130, 2, 1 ]
#new_shape= sliced_array.shape
#print(sliced_array)
#print(new_shape)



