import numpy as np 
import statistics as stats
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
print(np.concatenate([a1,a2])) #by default vertical
print(np.concatenate([a1,a2],axis=0)) #concatenate vertically
print(np.vstack([a1,a2])) #concatenate vertically
print(np.concatenate([a1,a2] , axis=1)) #concatenate horizontally
print(np.hstack([a1,a2])) #concatenate horizontally

a = np.array([20,30,40,40,30,20])
print(np.array_split(a,2))
print(np.array_split(a,3))
print(np.array_split(a,4))
print(np.array_split(a,4)[2])
print(np.array_split(a,3)[0])
print(np.array_split(a,2)[-1])
b = np.array([[1,2,3],[2,5,7]])
print(np.array_split(b,2))
print(np.array_split(b,3))
print(np.array_split(b,4))
print(np.array_split(b,4)[2])
print(np.array_split(b,3)[0])
print(np.array_split(b  ,2)[-1])

print()
print("Adding and removing elements")
arr = np.array([1,2,3,4,5])
print(np.append(arr,23))
print(np.append(arr,[78,99]))
print(np.insert(arr,2,98))
print(np.insert(arr,[2,5],[77,65]))
print(arr)
print(np.delete(arr,2)) #Element deleted at 2nd index i.e. 3
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.append(arr2 , 55)) #2d converted to 1d by its own
print(np.append(arr2 , [88 , 73 , 10]))
print(np.insert(arr2,1,45))
print(np.insert(arr2,[1],[45,92]))
print(np.insert(arr2,1,[66,99],axis=1)) #inserted in 2d array
print(np.insert(arr2,1,[66],axis=1)) 
print(arr2)
print(np.delete(arr2,2)) #2d to 1d , delete index 2
print(np.delete(arr2,2 , axis=1)) #3rd column with index 2 deleted 
print(np.delete(arr2,0,axis=0)) #1st row with index 0 is deleted 

print()
print("Sort , filter ans search techniques".center(50,"*"))
a = np.array([45,23,12,89,67])
print(np.sort(a))
print(np.where(a == 12))
print(np.where(a%3 == 0))
a2 = np.array([[5,1,3],[6,2,4]])
print(np.sort(a2))
print(np.where(a2==6))
sortedarr = np.array([11,23,45,67,89,90])
print(np.searchsorted(sortedarr,45))
arr=np.array([1,2,3,4,5,6])
print(arr[arr<4])
print(arr[arr%2==0])
filtr = [True,False,True,False,True,False]
print(arr[filtr])

print()
print("Aggregating functions in arrays".center(50,"*"))
a = np.array([12,57,82,34,60])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a)) #cumulative sum 
print(np.cumprod(a)) #cumulative product
price=np.array([10,20,30,40])
quantity=np.array([5,3,4,2])
print("Total amount = " , np.cumprod([price , quantity] , axis=0)[1].sum()) #first price*quantity , then their sum

print()
print("Statistical Functions".center(50,"*"))
data = np.array([20,50,35,60,10,95,10])
print(np.mean(data)) #sum of values / it's nu,ber
print(np.median(data)) #Central value
print(stats.mode(data)) #No mode in numpy library , so statistics library is imported , gives max occurring value
print(np.std(data)) #Standard deviation , if less means data is not at distance from mean i.e. data is less spread
print(np.var(data)) #Variance = square of std , used for quality check 
price=np.array([10,20,30,40])
quantity=np.array([5,3,4,2])
print(np.corrcoef(price,quantity)) 
#Correlation coefficient value : -1=inversely proportional , +1=proportional , 0=neutral
#corrcoef used to check dependency between two factors 