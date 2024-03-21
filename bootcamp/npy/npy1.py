import numpy as np

mylist = [1,2,3]
arr = np.array(mylist)
np.arange(0,11,2) #stepsize
np.arange(10)# 0-9 list
np.zeros(3)
np.zeros((3,4)) #3d
np.ones(1)
np.ones((3,4)) #3d
np.linspace(1,10,10) #equally space of total length n
np.eye(4)#identity matrix
np.random.rand(5) #random of (0,1) of length n
np.random.rand((5,5))#3d
np.random.randn(5)#return 1d array but with the distribution around 0
np.random.randn((5,5))
np.random.randint(1,100,10)#inc #exc #number of output
np.reshape(5,5) #you need 50 elements to reshape the array to this dimension
arr.max()#return max
arr.min()#return min
arr.argmax()#return argument of max
arr.argmin()#return argument of min
arr.shape#return shape of the array
arr.dtype#return dtype of the array