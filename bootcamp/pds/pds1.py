import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [1,2,3]
arr = np.array(my_data)
pd.Series(my_data,labels) #data,labels #data-numpyarray,array
pd.Series(dict)#convert the dictionary to series
pd.Series(arr)#this will just map 0->1st, 1->2nd thus act like list

ser1+ser2 # take single digit and do the operations
