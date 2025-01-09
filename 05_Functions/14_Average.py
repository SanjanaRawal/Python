def avg(*nums) :
    sum=0
    for num in nums :
        sum += num
    print("Average : " , sum/len(nums))

avg(5,20)
avg(30,15,18)
avg(4,8,12,8)