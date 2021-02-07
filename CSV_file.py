import numpy as np
#import numpy from genfrom
import urllib.request

#urllib.request.urlretrieve('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
                           #'ph_value.txt')

ph_data = np.genfromtxt('ph_value.txt', delimiter=';', skip_header=1)

print(ph_data)
ans=ph_data.shape
print(ans)
#transpose
trans= np.transpose(ph_data)
print(trans)
#sum
sum1=np.sum(ph_data)
print(sum1)
#mean/median/mode
me= np.median(ph_data)
print(me)
#round
r=np.round(ph_data)
print(r)
#max
maxx=np.max(ph_data)
print(maxx)