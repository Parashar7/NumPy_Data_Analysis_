import numpy as np

kanto= np.array([73,67,43])
weights=np.array([0.2,0.3,0.5])
#ans=array.shape
ans=np.dot(kanto,weights)
#ans1=ans.shape
ans1=(kanto*weights).sum()
ans2=kanto@weights
ans3=np.matmul(kanto,weights)
print(ans)
print(ans1)
print(ans2)
print(ans3)

