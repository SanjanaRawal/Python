import numpy as np 

arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))

arr2 = np.array([[1,2,3],[4,5,6],[8,9,0]])
print(arr2)
print(type(arr2))

print()
print("Slicing in arrays".center(50,"*"))
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[::-1])
print(arr[::2])
print(arr[1:5:3])
print()
print(arr2[0])
print(arr2[1])
print(arr2[0][2])
print(arr2[2][1])
print(arr2[1][1])
print(arr2[0:1][1:2])
print(arr2[0:2][0:2])

print()
print("Array Attributes".center(50,"*"))
print(np.shape(arr))
print(np.shape(arr2))
print(np.size(arr))
print(np.size(arr2))
print(np.ndim(arr))
print(np.ndim(arr2))
print(arr.dtype)
print(arr2.dtype)

print()
print("Inspecting the array".center(50,"*"))
print(arr.shape)
print(arr2.shape)
print(len(arr))
print(len(arr2))
print(arr.ndim)
print(arr2.ndim)
print(arr.size)
print(arr2.size)
print(arr.dtype)
print(arr2.dtype)
print(type(arr))
print(type(arr2))
print(arr.astype(float))
print(arr2.astype(str))

print()
a1 = np.array([[1,2] , [3,4]])
a2 = np.array([[5,3] , [9,1]])
a3 = np.array([3])
a4 = np.array([49 , 36 , 121 , 0 , 144])
print("Mathematical opeartions ans functions".center(50,"*"))
print(np.add(a1 , 2)) #Each element in array a1 incremented by 2
print(a1+a2) #Adds both matrix 
print(np.subtract(a1 , a2)) #Subtracts a2 from a1 
print(a1-10) #Each element of array a1 decremented by 10
print(np.multiply(a1 , 3)) #Each element multiplied by 3
print(a1*a2) # Each element in a1 multiplied with element at similar position in a2
print(np.divide(a1 , 10)) #Each element divides by 10
print(a1/a2) #Each element in a1 divided by corresponding position's element in a2
print(np.power(a1 , a3)) #Each element raised to power 3 
print(a2**a3) #Each element raised to power 3
print(np.sqrt(a4))

print()
print("Combining and splitting array".center(50,"*"))
a3 = np.array([1,2 , 3,4])
a4 = np.array([99 , 876])
print(np.concatenate([a3,a4]))
print(np.concatenate([a1,a2]))
print(np.concatenate([a1,a2],axis=0))
print(np.concatenate([a1,a2] , axis=1))
