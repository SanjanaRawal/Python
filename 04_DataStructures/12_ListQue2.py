nums = [ 23 , 89 , 12 , 56 , 0 , -34 , 77]
print(nums)

#Largest number
#Smallest number
#Add all numbers in list
max = nums[0]
min = nums[0]
sum = 0
for i in range(1 , len(nums) , 1) :
    if nums[i] > max : max = nums[i]
    if nums[i] < min : min = nums[i]
    sum += nums[i]
print("Largest number in list is " , max)
print("Smallest number in list is " , min)
print("Sum of all numbers in list is : " , sum)

#Print all numbers in the list individually
for num in nums :
    print(num)







