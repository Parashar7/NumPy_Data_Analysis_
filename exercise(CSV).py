import numpy as np

data = np.genfromtxt('phvalue.txt', delimiter=' ', skip_header=1)
sz = data.shape
print('Original data\n', data)
print(sz)

list1 = np.arange(0, 120+1, 10)

print('List to be multiplied\n',list1, list1.size)

result = np.matmul(data, list1)
print('Multiplied results\n', result)

final_results = np.concatenate((data, result.reshape(1599, 1)), axis=1)

print('Final array\n', final_results.round(), final_results.shape)

want = final_results[0, 3]

print(want)

sav = np.savetxt('phvalue.txt',
                 final_results,
                 fmt='%.2f',
                 header='"fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality";"FINAL RESULT"',
                 comments=''

                 )
